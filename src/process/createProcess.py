'''
多进程练习，创建多个进程
多进程适合于多核的计算机中，不用像多线程那样频繁切换
看一下Process类的构造方法：

__init__(self, group=None, target=None, name=None, args=(), kwargs={})
1
1
参数说明： 
group：进程所属组。基本不用 
target：表示调用对象。 
args：表示调用对象的位置参数元组。 
name：别名 
kwargs：表示调用对象的字典。
'''
import multiprocessing

def do(m):
    name=multiprocessing.current_process().name#获取当前执行的进程的名称
    print(name,"Staring")
    print("run worker",m)
    return 
    
if __name__ == '__main__' :
  numList = []
  for i in range(5) :
    p = multiprocessing.Process(target=do, args=(i,))#创建一个子进程，指定进程的执行函数和并传入函数的参数
    numList.append(p)#将进程添加到列表中去
    p.start()
    p.join()#让进程当前进程执行完，才去执行下一个进程
    print("process end")