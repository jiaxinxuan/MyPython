'''
Created on 2017年5月23日

@author: Administrator
'''
# import urllib.request
# import urllib
#  
# url = "http://www.baidu.com"
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# urllib.parse.urlencode(data)
# print(data)

import urllib
import urllib.request
  
# data={}
# data['word']='Jecvay Notes'
#  
# url_values=urllib.parse.urlencode(data)
# print(url_values)
# url="http://www.baidu.com/s?"
# full_url=url+url_values
# print(full_url)
# data=urllib.request.urlopen(full_url).read()
# data=data.decode('UTF-8')
# print(data)

url="http://www.baidu.com"
data=urllib.request.urlopen(url).read()
data.decode('UTF-8')
print(data)