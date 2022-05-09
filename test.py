import unittest
import uuid

from defipay.client import Client
from defipay.config import SANDBOX
from defipay.signer.local_signer import LocalSigner


class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(signer=LocalSigner("cbc7856ce7c836399dd886a6e2deb905b776a6029840f8254e5a5ce10f280c2e"),
                             env=SANDBOX,
                             debug=True)

    def get_member_trans_no(self):
        uuid_str = str(uuid.uuid4())
        return ''.join(uuid_str.split('-')).upper()

    def test_create_order(self):
        response = self.client.create_order("http://xcsewvb.ao/nhhcn", "http://xcsewvb.ao/nhhcn"
                                            , self.get_member_trans_no(), "1000", "USDT", "2")
        self.assertTrue(response.success)

    def test_query_order(self):
        response = self.client.query_order("29N3FVHO")
        self.assertTrue(response.success)

    def test_create_payout_order(self):
        response = self.client.create_payout_order("http://xcsewvb.ao/nhhcn", self.get_member_trans_no(), "1000"
                                                   , "USDT", "2","0x3531C5F7540aDC5e5d640De11DE524cD379CC717",None)
        self.assertTrue(response.success)

    def test_query_payout_order(self):
        response = self.client.query_payout_order("EI68E4Z6")
        self.assertTrue(response.success)

    def test_query_bill_currency(self):
        response = self.client.query_bill_currency(1,10)
        self.assertTrue(response.success)

    def test_query_pay_currency(self):
        response = self.client.query_pay_currency(1,10)
        self.assertTrue(response.success)

    def test_query_crypto_amount(self):
        response = self.client.query_crypto_amount()
        self.assertTrue(response.success)

    def test_query_order_list(self):
        response = self.client.query_order_list(1,10)
        self.assertTrue(response.success)

    def test_get_order_detail(self):
        response = self.client.get_order_detail('29N3FVHO')
        self.assertTrue(response.success)

    def test_query_rate(self):
        response = self.client.query_rate("ETH","USDT")
        self.assertTrue(response.success)


if __name__ == '__main__':
    unittest.main()
