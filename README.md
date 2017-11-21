# yqt-sdk-python
# 平台服务介绍

> YQT-SDK-Python是基于[YQT](http://doc.jia007.com)接口封装的开发工具包。她屏蔽了大部分细节、简化了接入流程、同时提供了一些便捷的方法。帮助开发者在接入过程中避开一些常见的问题，让开发者快速接入[YQT](http://doc.jia007.com)的服务。

> *注: 该开发工具包仅支持Python语言，其他语言开发者可以参照[YQT](http://doc.jia007.com)的官方文档。*

##  快速接入

### 准备工作

1. 说的再好都不如一个栗子吃得饱，让我们一起来看下干货。

### DEMO 

下面我们使用Python作为开发语言，对接[YQT](http://doc.jia007.com)的用户消费接口。

```python
import AesUtils
import Client
import json
# coding=utf-8

#请求服务器地址
url = "https://api.jia007.com/api-center/rest/v1.0/yqt/consume"

#商户编号
appKey = "1051100110000069a"

#商户秘钥
secretKey = "c93b77ac5c7c4937"

#请求数据
request = {}
request['requestNo']='1234567890qwertyui12'
request['payTool']='WECHAT_SCAN'
request['productDesc']='ceshi'
request['orderAmount']='0.01'
request['serverCallbackUrl']='http://www.qq.com'
request['sceneType']='MIS'
request['clientIp']='192.168.1.1'
request['currency']='CNY'
request['orderDate']='2017-11-17 11:28:04'
request['merchantNo']='1051100110000070'
request['productName']='测试'

#转换为json请求数据,解决中文乱码
requestJson = json.dumps(request,ensure_ascii=False)

#对请求数据进行加密
data = AesUtils.AESUtil.encryt(requestJson,secretKey)

#发送请求
response = Client.Client.post(url,data,appKey)

if "code" in response:
# 由于未请求到业务系统，直接返回未加密字符串
print  response
else:
#正常解密响应数据
response = AesUtils.AESUtil.decrypt(response,secretKey)
print  response

#Console打印日志为：
{
    "code":"1",
    "orderAmount":"0.01",
    "orderNo":"11171114183109692912",
    "redirectUrl":"weixin://wxpay/bizpayurl?pr\u003d7PYdx1J",
    "message":"受理成功",
    "status":"PROCESS"
}
```