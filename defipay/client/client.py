import json
import time
from urllib.parse import urlencode, unquote

import requests

from defipay.client.api_response import ApiResponse
from defipay.config import Env
from defipay.error.api_error import ApiError
from defipay.signer.api_signer import ApiSigner
from defipay.signer.local_signer import verify_ecdsa_signature


class Client(object):

    def __init__(self, signer: ApiSigner, env: Env, debug: bool = False):
        self.api_signer = signer
        self.env = env
        self.debug = debug

    def sort_params(self, params: dict) -> str:
        params = [(key, val) for key, val in params.items()]

        params.sort(key=lambda x: x[0])
        return unquote(urlencode(params))

    def remove_none_value_elements(self, input_dict: dict) -> dict:
        if type(input_dict) is not dict:
            return {}
        result = {}
        for key in input_dict:
            tmp = {}
            if input_dict[key] is not None:
                if type(input_dict[key]).__name__ == 'dict':
                    tmp.update({key: self.remove_none_value_elements(input_dict[key])})
                else:
                    tmp.update({key: input_dict[key]})
            result.update(tmp)
        return result

    def verify_response(self, response: requests.Response) -> (bool, dict):
        content = response.content.decode()
        success = True
        try:
            timestamp = response.headers["BIZ-TIMESTAMP"]
            signature = response.headers["BIZ-RESP-SIGNATURE"]
            if self.debug:
                print(f"response <<<<<<<< \n content: {content}\n headers: {response.headers} \n")
            success = verify_ecdsa_signature("%s|%s" % (content, timestamp), signature, self.env.defipayPub)
        except KeyError:
            pass
        return success, json.loads(content)

    def request(
            self,
            method: str,
            path: str,
            params: dict
    ) -> ApiResponse:
        method = method.upper()
        nonce = str(int(time.time() * 1000))
        params = self.remove_none_value_elements(params)
        content = f"{method}|{path}|{nonce}|{self.sort_params(params)}"
        sign = self.api_signer.sign(content)

        headers = {
            "Biz-Api-Key": self.api_signer.get_public_key(),
            "Biz-Api-Nonce": nonce,
            "Biz-Api-Signature": sign,
        }
        url = f"{self.env.host}{path}"
        if self.debug:
            print(f"request >>>>>>>>\n method: {method} \n url: {url} \n params: {params} \n headers: {headers} \n")

        if method == "GET":
            resp = requests.get(url, params=urlencode(params), headers=headers)
        elif method == "POST":
            resp = requests.post(url, data=params, headers=headers)
        else:
            raise Exception("Not support http method")
        verify_success, result = self.verify_response(resp)
        if not verify_success:
            raise Exception("Fatal: verify content error, maybe encounter mid man attack")
        print("content:" + content)
        print("sig:" + sign)
        print("nonce:" + nonce)
        print("Response" + str(result))

        success = result['success']
        if success:
            return ApiResponse(True, result, None)
        else:
            exception = ApiError(result['code'], result['msg'], '')
            return ApiResponse(False, None, exception)

    def create_order(self, notifyUrl: str, returnUrl: str, memberTransNo: str, amount: str, currency: str
                     , tokenIds: str):
        return self.request("POST", "/v1/external/pay/create", {
            "notifyUrl": notifyUrl,
            "returnUrl": returnUrl,
            "memberTransNo": memberTransNo,
            "amount": amount,
            "currency": currency,
            "tokenIds": tokenIds
        })

    def query_order(self, transNo: str):
        return self.request("POST", "/v1/external/pay/query", {
            "transNo": transNo
        })

    def create_payout_order(self, notifyUrl: str, memberTransNo: str, amount: str, currency: str
                            , tokenId: str, toAddress: str, payAmount: str):
        return self.request("POST", "/v1/external/payout/create", {
            "notifyUrl": notifyUrl,
            "memberTransNo": memberTransNo,
            "amount": amount,
            "currency": currency,
            "tokenId": tokenId,
            "toAddress": toAddress,
            "payAmount": payAmount
        })

    def query_payout_order(self, transNo: str):
        return self.request("POST", "/v1/external/payout/query", {
            "transNo": transNo
        })

    def query_bill_currency(self, offset: int, limit: int):
        return self.request("POST", "/v1/external/billCurrency/query", {
            "offset": offset,
            "limit": limit
        })

    def query_pay_currency(self, offset: int, limit: int):
        return self.request("POST", "/v1/external/token/query", {
            "offset": offset,
            "limit": limit
        })

    def query_crypto_amount(self):
        return self.request("GET", "/v1/external/account/query", {})

    def query_order_list(self, offset: int, limit: int):
        return self.request("POST", "/v1/external/order/list", {
            "offset": offset,
            "limit": limit
        })

    def get_order_detail(self, transNo: str):
        return self.request("GET", "/v1/external/order/getDetail", {
            "transNo": transNo
        })

    def query_rate(self, base: str, quote: str):
        return self.request("POST", "/v1/external/rate/query", {
            "base": base,
            "quote": quote
        })
