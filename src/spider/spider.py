'''
Created on 2017年5月23日

@author: Administrator
抓取百度的首页并保存到磁盘中

import urllib.request
import urllib
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
f=open(file="F:/test.html",mode="a",encoding="UTF-8")#必须指定要创建的文件和要写入的数据的格式一致
f.write(data)
f.flush()
f.close()
print(data)
'''


'''
向百度发出查询请求，抓取查询结果
import urllib
import urllib.request
import sys,os
data={}
data['word']='Jecvay Notes'
url_values=urllib.parse.urlencode(data)
print(url_values)
url="http://www.baidu.com/s?"
full_url=url+url_values
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')#对抓取到的内容进行编码
print(data)
'''


'''
python读取文件begin
'''
# try:
#      fsock=open(file="F:/data/service/seo/product/file/index.html",encoding="UTF-8",mode="r",)#读取文件
# #      fsock=open(file="F:/data/service/seo/product/file/index123.html",encoding="UTF-8",mode="a+")
# except IOError:
#      print ("The file don't exist, Please double check!")
#      exit()
# fsock.flush()
# content=fsock.read()
# print(content)
# print(fsock.name)
# print(fsock.mode)
# fsock.close()
'''
python读取文件end
'''
'''
抓取网页中的所有连接
Python3中urllib和urllib2都集成在同一个包urllib中了，同时urllib也被拆分为urllib.request,urllib.parse,urllib.error
等磨矿

'''
import re

import urllib.request


#获取链接地址中的所有链接
def DFS(url):
    website = urllib.request.urlopen(url)
    #read html code
    html = website.read().decode("UTF-8")
    #use re.findall to get all the links
    links =re.findall('"((http|ftp)s?://.*?)"', html)
    print(url,"网址下所有链接",links)
    while len(links):
        link=list.pop(links)
        try:
            DFS(link[0])
        except:
            continue;
    return;

#connect to a URL
try:
    i=0;
    url="http://www.caixin.com/"
    website = urllib.request.urlopen(url=url,timeout=10)
    #read html code
    html = website.read().decode("UTF-8")
    #use re.findall to get all the links
    links =re.findall('"((http|ftp)s?://.*?)"', html)
    print(links)
    while len(links):
        link=list.pop(links)
        i+=1
        print(link,"第",i,"个链接")
        if "jpg" not in link[0] and "gif" not in link[0]:
            DFS(link[0])
except:
    print("异常退出")