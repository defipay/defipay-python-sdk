# Defipay python API

defipay-python-api 是一個輕量級的 Python 庫，用于與[Defipay API](http://doc.defipay.biz/)交互，提供完整的 API 覆蓋。

* [安裝](#安裝)
* [測試](#測試)
* [用法](#用法)
  * [初始化](#初始化)
     * [生成密鑰對](#生成密鑰對)
     * [初始化 RestClient](#初始化-restclient)
     * [初始化 ApiSigner](#初始化-apisigner)
  * [充值](#充值)
     * [充值請求下單](#充值請求下單)
     * [充值交易查詢](#充值交易查詢)
  * [提現](#提現)
     * [提現請求下單](#提現請求下單)
     * [提現交易查詢](#提現交易查詢)
  * [交易](#交易)
     * [獲取已入賬的交易詳情](#獲取已入賬的交易詳情)
     * [通過ID查詢獲取已確認的交易記錄](#通過ID查詢獲取已確認的交易記錄)
  * [賬戶余額查詢](#賬戶余額查詢)
     * [商戶賬戶余額查詢](#商戶賬戶余額查詢)
     * [支持賬單幣種查詢](#支持賬單幣種查詢)
     * [支持支付幣種查詢](#支持支付幣種查詢)
  * [匯率查詢](#匯率查詢)
     * [幣種匯率查詢](#幣種匯率查詢)
 

## 安裝

```
pip install defipay
```


## 測試

```
python -m unittest test.ClientTest
```

## 用法

### 初始化

#### 生成密鑰對

```python
from defipay.signer.local_signer import generate_new_key
api_secret, api_key = generate_new_key()
print(api_secret)
print(api_key)
```

apiKey的使用方法請參考[鏈接](http://doc.defipay.biz/index.html#title1_child2)

#### 初始化-restClient

```python
from defipay.client import Client
from defipay.config import SANDBOX
from defipay.signer.local_signer import LocalSigner
client = Client(signer=signer, env=SANDBOX, debug=True)
```

#### 初始化-apiSigner


`ApiSigner` 可以通過實例化

```python
from defipay.signer.local_signer import LocalSigner
LocalSigner("API_SECRET")
```

在某些情況下，您的私鑰無法導出，例如，您的私鑰在 aws kms 中，您應該通過實現`ApiSigner`接口傳入您自己的實現：


### 充值

#### 充值請求下單
```python
client.create_order("http://xcsewvb.ao/nhhcn", "http://xcsewvb.ao/nhhcn"
                                            , "testasdafasf002", "1000", "USDT", "2")
```
<details>
<summary>響應視圖</summary>


```python
CreateOrderResponse{cashierUrl='http://47.97.49.47/customer/#/order/LBGL6HAH', tokenInfo=[PayOrderAddressInfoDTO{address='0x62b0f4dcc559a57482f7cf800e10ab9e72e270ae', amount='0', shortName='ETH', displayName='ETH', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/ba40da70bed74489a7ed6adaed495763.png', coinType='Mainnet', chainId=null, chainAssertDecimal=18, chainAssertId=''}], memberTransNo='testasdafasf001', currency='ETH', amount='0.01', transNo='LBGL6HAH'}
```
</details>

#### 充值交易查詢
```python
client.query_order("29N3FVHO")
```
<details>
<summary>響應視圖</summary>


```python
[OrderQueryResponse{id=null, transNo='UG45OID2', memberTransNo='testasdafasf001', tokenId=null, shortName='null', billAmount='null', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='null', memo='null', comment='null', confirmNum=null, state=null, scanUrl='null', expiredTime=null, settleTime=null}]
```
</details>


### 提現
#### 提現請求下單
```python
client.create_payout_order("http://xcsewvb.ao/nhhcn", "FSA7SDF798AS7DF987A9FSD", "1000"
                                                   , "USDT", "2","0x3531C5F7540aDC5e5d640De11DE524cD379CC717",None)
```
<details>
<summary>響應視圖</summary>

```python
CreatePayoutOrderResponse{transNo='5NONKD04', memberTransNo='null', currency='null', amount='null', tokenId=null, tokenAmount='null'}
```
</details>

#### 提現交易查詢
```python
client.query_payout_order("EI68E4Z6")
```
<details>
<summary>響應視圖</summary>


```python
PayoutOrderQueryResponse{id=null, transNo='UG45OID2', memberTransNo='testasdafasf001', tokenId=null, shortName='null', billAmount='null', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='null', memo='null', comment='null', confirmNum=null, state=null, scanUrl='null', expiredTime=null, settleTime=null}
```
</details>

### 交易

#### 獲取已入賬的交易詳情
```python
client.query_order_list(1,10)
```
<details>
<summary>響應視圖</summary>


```python
[OrderQueryResponse{id=529, transNo='S93XDMQH', memberTransNo='testasdafasf001', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=528, transNo='LBGL6HAH', memberTransNo='testasdafasf001', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=256, transNo='5NONKD04', memberTransNo='testasdafasf002', tokenId=null, shortName='ETH', billAmount='0.01', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='0x3531C5F7540aDC5e5d640De11DE524cD379CC717', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=527, transNo='5TPBCF4O', memberTransNo='testasdafasf001', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=526, transNo='UG45OID2', memberTransNo='testasdafasf001', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=499, transNo='0ROTWJWK', memberTransNo='CB1d9Ed8-E203-7Aa3-16fF-b71CdBe466e00955', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=497, transNo='JY0I5FBC', memberTransNo='CB1d9Ed8-E203-7Aa3-16fF-b71CdBe466e00955', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=491, transNo='O33XPB3D', memberTransNo='CB1d9Ed8-E203-7Aa3-16fF-b71CdBe466e005', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=490, transNo='QWG4G6OD', memberTransNo='CB1d9Ed8-E203-7Aa3-16fF-b71CdBe466e00955', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}, OrderQueryResponse{id=489, transNo='0D49NLA0', memberTransNo='CB1d9Ed8-E203-7Aa3-16fF-b71CdBe466e00955', tokenId=null, shortName='', billAmount='', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='', memo='null', comment='null', confirmNum=null, state=300, scanUrl='null', expiredTime=null, settleTime=0}]
```
</details>

#### 通過ID查詢獲取已確認的交易記錄
```python
client.get_order_detail('29N3FVHO')
```
<details>
<summary>響應視圖</summary>


```python
OrderQueryResponse{id=84, transNo='HHJQ6T3V', memberTransNo='test20220413017', tokenId=null, shortName='ETH', billAmount='0.001', billCurrency='null', txHash='null', blockNumber=null, fromAddress='null', toAddress='0x88a611Ceb5Cb3f0Fc002261F47CC85EbEd304412', memo='null', comment='null', confirmNum=null, state=200, scanUrl='null', expiredTime=null, settleTime=1650339701}
```
</details>

### 賬戶余額查詢
#### 商戶賬戶余額查詢
```python
client.query_crypto_amount()
```
<details>
<summary>響應視圖</summary>


```python
[MemberUserVirtualAccountInfoResponse{totalAmount=1.100000000000000000000000000000, frozenAmount=0E-30, availableAmount=1.100000000000000000000000000000, tokenId=1, shortName='BTC', name='BTC', displayName='BTC', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/8f6e5e2382f94028b87307ad5c73c52e.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=-1.566048866588656755000000000000, frozenAmount=-2.125287338844321266000000000000, availableAmount=0.559238472255664511000000000000, tokenId=2, shortName='ETH', name='ETH', displayName='ETH', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/ba40da70bed74489a7ed6adaed495763.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=1.000000000000000000000000000000, frozenAmount=0E-30, availableAmount=1.000000000000000000000000000000, tokenId=3, shortName='USDT', name='Tether', displayName='USDT-ERC20', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/1b88c0c2dba04080bd3165843de3ffae.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=919.000000000000000000000000000000, frozenAmount=0E-30, availableAmount=919.000000000000000000000000000000, tokenId=25, shortName='TRX', name='TRON', displayName='TRX', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/c205901ff60f4d588d4617bbaa0bc939.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=1.000000000000000000000000000000, frozenAmount=0E-30, availableAmount=1.000000000000000000000000000000, tokenId=30, shortName='XLM', name='Stellar Lumens', displayName='XLM', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/f15e6a83d9e34060b1cbb84c628aa2ec.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=10.000000000000000000000000000000, frozenAmount=0E-30, availableAmount=10.000000000000000000000000000000, tokenId=31, shortName='USDT', name='Tether', displayName='USDT-TRC20', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/1b88c0c2dba04080bd3165843de3ffae.png'}, MemberUserVirtualAccountInfoResponse{totalAmount=0E-30, frozenAmount=0E-30, availableAmount=0E-30, tokenId=42, shortName='TETH_CTT', name='Defipay Test Token', displayName='TETH_CTT', logoUrl='https://ipi-cdn.oss-cn-hangzhou.aliyuncs.com/tadle_v1.1/user/avater/e9a72a3480054fd7968d84617c4c0db2.jpg'}, MemberUserVirtualAccountInfoResponse{totalAmount=0E-30, frozenAmount=0E-30, availableAmount=0E-30, tokenId=12, shortName='DOGE', name='DogeCoin', displayName='DOGE', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/ec90d3d5635747b199967ce06a5be4c3.png'}]
```
</details>

#### 支持賬單幣種查詢
```python
client.query_bill_currency(1,10)
```
<details>
<summary>響應視圖</summary>


```python
CoinApiAssetInfoDTO{assertId='AED', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='AUD', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='BRC', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='BYN', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='CAD', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='CHF', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='CLP', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='DEM', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='DKK', typeIsCrypto=0}, CoinApiAssetInfoDTO{assertId='ESP', typeIsCrypto=0}
```
</details>

#### 支持支付幣種查詢
```python
client.query_pay_currency(1,10)
```
<details>
<summary>響應視圖</summary>


```python
[ChainTokenInfoDTO{id=1, name='BTC', displayName='BTC', shortName='BTC', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/8f6e5e2382f94028b87307ad5c73c52e.png', chainAssertId='', chainAssertDecimal='6'}, ChainTokenInfoDTO{id=2, name='ETH', displayName='ETH', shortName='ETH', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/ba40da70bed74489a7ed6adaed495763.png', chainAssertId='', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=3, name='Tether', displayName='USDT-ERC20', shortName='USDT', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/1b88c0c2dba04080bd3165843de3ffae.png', chainAssertId='0xdac17f958d2ee523a2206206994597c13d831ec7', chainAssertDecimal='6'}, ChainTokenInfoDTO{id=4, name='Binance Coin', displayName='BNB', shortName='BNB', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/6300d391da1642c58c6673f32235db89.png', chainAssertId='null', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=5, name='USDC', displayName='USDC-ERC20', shortName='USDC', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/b5afa9c1d46842cea775d3e63c9287b7.png', chainAssertId='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', chainAssertDecimal='6'}, ChainTokenInfoDTO{id=6, name='Ripple', displayName='XRP-BEP20', shortName='XRP', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/7df1c4bc20054894b52b4aa6a7ae1e81.png', chainAssertId='0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=7, name='Cardano', displayName='ADA-BEP20', shortName='ADA', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/35d6f3167e9c4a9dae0ef34c50a1deb0.png', chainAssertId='0x3ee2200efb3400fabb9aacf31297cbdd1d435d47', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=8, name='Solana', displayName='SOL', shortName='SOL', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/068abeb1076c40189d64c69cf70ed6e6.png', chainAssertId='null', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=9, name='Luna Coin', displayName='LUNA', shortName='LUNA', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/a8a96dd9240c425291bb87178aae935c.png', chainAssertId='null', chainAssertDecimal='18'}, ChainTokenInfoDTO{id=10, name='AVAX', displayName='AVAX-C', shortName='AVAX', logoUrl='https://defipay-test.oss-cn-hangzhou.aliyuncs.com/defipay_v_1.0/62f25f5cf608415587a7cda95d9238c0.png', chainAssertId='null', chainAssertDecimal='18'}]
```
</details>


### 匯率查詢
#### 幣種匯率查詢
```python
client.query_rate("ETH","USDT")
```
<details>
<summary>響應視圖</summary>


```python
RateDTO{rate='2941.9196987295191192656236054', rateTime=1651723212}
```
</details>


