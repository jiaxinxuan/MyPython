import datetime  
import threading  
from time import ctime, sleep  

import urllib.request


def t1(func):  
  for i in range(50):  
    starttime = datetime.datetime.now()  
    url = "http://tag.caixin.com/news/homeInterface.jsp?subject=100589266&start=0&count=100&picdim=_145_97&type=2&callback=?"
    f=urllib.request.urlopen(url)  
    s=f.read()  
    endtime = datetime.datetime.now()  
    print (i, func, s, (endtime - starttime).microseconds / 1000) 
    sleep(1)  
   
   
if __name__ == '__main__':  
  threads=[]  
  for i in range(50):  
    name = "t%s" % (i)  
    name = threading.Thread(target=t1,args=(i,))  
    threads.append(name)  
  for t in threads:  
    t.setDaemon(True)  
    t.start()  
  t.join()  
