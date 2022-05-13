from defipay.config.env import Env

SANDBOX = Env(host="https://api-test.defipay.biz/api-service",
              defipayPub="0314c127b69c03545b49aaf365c56575ce9b1640cad8eb6ca47c34c8322fe9f4d4")
PROD = Env(host="https://api.defipay.biz/api-service",
           defipayPub="0314c127b69c03545b49aaf365c56575ce9b1640cad8eb6ca47c34c8322fe9f4d4")
