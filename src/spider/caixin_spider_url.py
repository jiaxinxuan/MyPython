"""
抓取网页中的所有连接
Python3中urllib和urllib2都集成在同一个包urllib中了，同时urllib也被拆分为urllib.request,urllib.parse,urllib.error
等磨矿
"""

import re
import urllib.request


# 获取链接地址中的所有链接

# 利用元祖的键值唯一的特性排除重复
map = {}


def dfs(url):
    try:
        website = urllib.request.urlopen(url=url, timeout=2)
        html = website.read().decode("UTF-8")
        links =re.findall('"((http|ftp)s?://.*?)"', html)
    except Exception as er:
        print(er)
        return
    print("当前链接：", url, links.__len__())
    while len(links):
        link = list.pop(links)
        print(link[0])
        if "PDF" not in link[0] and "jpg" not in link[0] and "png" not in link[0]:
            if link[0] not in map:
                map[link[0]] = 1
                dfs(link[0])
            else:
                return

# connect to a URL



i = 0;
url = "http://www.caixin.com/"
website = urllib.request.urlopen(url=url, timeout=10)
html = website.read().decode("UTF-8")
links = re.findall('"((http)s?://.*?)"', html)
print(links, links.__len__(), sep="\n", end="\n")
while len(links):
    link = list.pop(links)
    i += 1
    print(link, "第", i, "个链接", end="\n")
    if "PDF" not in link[0] and "jpg" not in link[0] and "png" not in link[0]:
        dfs(link[0])
