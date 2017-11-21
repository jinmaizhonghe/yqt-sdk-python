# -*- coding=utf-8-*-
# Autrhor: YQT by pengfei.he
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
request['productName']='鹏飞测试'
#转换位json请求数据,解决中文乱码
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

#返回数据
#解密原始数据：{"code":"1","orderAmount":"0.01","orderNo":"11171114183109692912","redirectUrl":"weixin://wxpay/bizpayurl?pr\u003d7PYdx1J","message":"受理成功","status":"PROCESS"}



