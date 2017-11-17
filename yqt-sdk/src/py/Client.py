# -*- coding=utf-8-*-
# Autrhor: YQT by pengfei.he
import urllib
import urllib2

class Client:

    @staticmethod
    def post(url,data,appKey):
        url = url+"?appKey="+appKey+"&data="+data
        print "请求地址"+url
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res
