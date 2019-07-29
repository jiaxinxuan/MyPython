"""
简单Python爬虫，抓取b站某个电影的评论数据，生成词云
"""
import datetime
import urllib.parse
import urllib.request
import urllib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from openpyxl import Workbook
import json
import jieba
import smtplib

wb = Workbook()
dest_filename = '信阳二手房数据.xlsx'
ws1 = wb.active
ws1.title = "信阳二手房数据"
records = []


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
        inFile = open(file=inputFile, mode="r", encoding="UTF-8")
        # 以写的方式打开该文件
        outFile = open(file=outPutFile, mode="w", encoding="UTF-8")
        # 循环遍历打开的文件，取出其中每行，并对每行进行分词
        for eachLine in inFile:
            # 此句取某一行的数据，并且去除两端的空格，并以utf-8的形式编码
            line = eachLine.strip().encode("UTF-8", "ingore")
            wordList = jieba.cut(line);
            # 将当前行得到的分词数据，写入到输出文件中去
            outstr = ''
            for word in wordList:
                outstr += word
                outstr += "/"
            outFile.write(outstr.strip() + "\n")
    except Exception as ex:
        print("文件处理出错", ex)
    finally:
        inFile.close()
        outFile.close()


def writer_excel(replies):
    for i in range(len(replies)):
        record = replies[i]
        ws1['A%s' % (i + 1)] = record['id']
        ws1['B%s' % (i + 1)] = record['title']
        ws1['C%s' % (i + 1)] = record['image']
        ws1['D%s' % (i + 1)] = str(record['bedroom'])+'室'+str(record['livingroom'])+'厅'
        ws1['F%s' % (i + 1)] = str(record['area'])+str(record['street'])
        ws1['G%s' % (i + 1)] = str(record['price'])+record['unit']
        ws1['H%s' % (i + 1)] = record['created']
        ws1['I%s' % (i + 1)] = record['sale_time']
        ws1['J%s' % (i + 1)] = ''.join(record['ts'])
        ws1['K%s' % (i + 1)] = record['plot_name']
        ws1['L%s' % (i + 1)] = record['type']
        ws1['M%s' % (i + 1)] = str(record['ave_price'])+'元'
        ws1['N%s' % (i + 1)] = str(record['size']) + '平'
    wb.save(filename=dest_filename)


def sed_email():
    sender = '552387367@qq.com'
    receivers = ['552387367@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att = MIMEText(open(dest_filename, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", dest_filename))
    message.attach(att)
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login("552387367@qq.com", 'ueettppzccnwbfad')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print( "邮件发送成功")


if __name__ == '__main__':
    for i in range(0, 3):
        print(i)
        url = 'https://www.xyfcw.com/api/resoldwapapi/esflist?page=' + str(i);
        result = login_get(url)
        jsons = json.loads(result, encoding='UTF-8')
        replies = jsons['data']['list']
        records.extend(replies)
    writer_excel(records)
    sed_email()
