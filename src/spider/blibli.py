"""
简单Python爬虫，抓取b站某个电影的评论数据，生成词云
"""

import urllib.parse
import urllib.request
import urllib
from wordcloud import WordCloud
import json
import jieba
import matplotlib.pyplot as plt


# get请求


def login_get(url):
    response = urllib.request.urlopen(url)
    text = response.read()
    return text.decode('UTF-8')
# post 请求


def login_post(url, header, data):
    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url, data=data, headers=header)
    response = urllib.request.urlopen(req, timeout=5)
    return response.read().decode('UTF-8')
#   写入文件


def output_file(content, outPutFile):
    outfile = open(file=outPutFile, mode="a", encoding="UTF-8")  # 以写的方式打开该文件
    outfile.write(content)
    outfile.flush()

# 结巴分词


def sliptsentence(inputFile, outPutFile):
    try:
        # 以读的方式打开该文件
        inFile=open(file=inputFile, mode="r",encoding="UTF-8")
        # 以写的方式打开该文件
        outFile=open(file=outPutFile,mode="w",encoding="UTF-8")
        # 循环遍历打开的文件，取出其中每行，并对每行进行分词
        for eachLine in inFile:
            # 此句取某一行的数据，并且去除两端的空格，并以utf-8的形式编码
            line=eachLine.strip().encode("UTF-8","ingore")
            wordList=jieba.cut(line);
            # 将当前行得到的分词数据，写入到输出文件中去
            outstr=''
            for word in wordList:
                outstr+=word
                outstr+="/"
            outFile.write(outstr.strip()+"\n")
    except Exception as ex:
        print("文件处理出错",ex)
    finally:
       inFile.close()
       outFile.close()


if __name__ == '__main__':
    for i in range(1,38):
        url='http://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn='+str(i)+'&type=1&oid=2651396&sort=0&_=1510978290823'
        result = login_get(url)
        jsons = json.loads(result, encoding='UTF-8')
        replies = jsons['data']['replies']
        message = ''
        for user in replies:
            content=user['content']
            message += content['message']+'\n'
            print(content['message'])
        output_file(message,'/home/jia/content.log')
    sliptsentence('/home/jia/content.log', '/home/jia/jieba.json')
    f = open(u'/home/jia/jieba.json', 'r', encoding='UTF-8').read()
    wordcloud = WordCloud(background_color="white", width=1000, height=860,
                          margin=2, font_path='/home/jia/bole.ttf').generate(f)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('test.png')

