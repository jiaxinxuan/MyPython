"""
　　 python3.4
    模拟登录郑州公积金网站，查询缴存至月份。
"""
import urllib.parse
import urllib.request
import urllib
from bs4 import BeautifulSoup as BS
import getpass
import json

# get方法登录


def login_get(url):
    response = urllib.request.urlopen(url)
    text = response.read()
    return text.decode('UTF-8')

# post方法登录


def login_post(url, header, data):
    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url, data=data, headers=header)
    response = urllib.request.urlopen(req, timeout=5)
    return response.read().decode('UTF-8')
# 模拟登录财新


if __name__ == '__main__':
    # zhiHuLogin()
    posturl = 'https://gateway.caixin.com/api/ucenter/user/v1/loginJsonp?account=15037006133&password=1330ce633988b5b25c0b808706c52176&device=CaixinWebsite&deviceType=5&unit=1&_=1510909310122'
    result = login_get(posturl)
    print(result)