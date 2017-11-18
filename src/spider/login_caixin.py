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
import jieba

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
#   写入文件
def outputfile(content,outPutFile):
    outFile = open(file=outPutFile, mode="a", encoding="UTF-8")  # 以写的方式打开该文件
    outFile.write(content)
    outFile.flush()

# 结巴分词

def sliptsentence(inputFile,outPutFile):
    try:
        inFile=open(file=inputFile, mode="r",encoding="UTF-8")#以读的方式打开该文件
        outFile=open(file=outPutFile,mode="w",encoding="UTF-8")#以写的方式打开该文件
        '''
                循环遍历打开的文件，取出其中每行，并对每行进行分词
        '''
        for eachLine in inFile:
            line=eachLine.strip().encode("UTF-8","ingore")#此句取某一行的数据，并且去除两端的空格，并以utf-8的形式编码
            wordList=jieba.cut(line);
            '''
                        将当前行得到的分词数据，写入到输出文件中去
            '''
            outstr=''
            for word in wordList:
                outstr+=word
                outstr+="/"
            outFile.write(outstr.strip()+"\n")
    except :
        print("文件处理出错")
    finally:
       inFile.close()
       outFile.close()



if __name__ == '__main__':
    # posturl = 'https://gateway.caixin.com/api/ucenter/user/v1/loginJsonp?account=15037006133&password=1330ce633988b5b25c0b808706c52176&device=CaixinWebsite&deviceType=5&unit=1&_=1510909310122'
    # result = login_get(posturl)
    # print(result)
    for i in range(1,38):
        url='http://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn='+str(i)+'&type=1&oid=2651396&sort=0&_=1510978290823'
        result = login_get(url)
        print(result)
        jsons=json.loads(result, encoding='UTF-8')
        replies=jsons['data']['replies']
        message = ''
        for user in replies:
            content=user['content']
            message+=content['message']+'\n'
            print(content['message'])
        outputfile(message,'/home/jia/content.log')



    sliptsentence('/home/jia/content.log','/home/jia/jieba.json')

