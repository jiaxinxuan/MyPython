'''
Created on 2017年6月20日

@author: Administrator
'''
from multiprocessing import Pool,cpu_count
import time
#计算平方和
def fn(n):
    time.sleep(1)#必须设置休眠时间，模拟运算操作，否则看不出来效果
    return n*n
if __name__ == '__main__':
    count=cpu_count()
    print("cup内核数",count)
    testFl=[1,2,3,4,5]
    print("顺序执行")
    s=time.time()
    for n in testFl:
        fn(n)
    e1=time.time()
    print("顺序执行时间",int(e1-s),s,e1)
    
    #并发执行
    pool=Pool(count)
    print("并发执行")
    rl=pool.map(fn,testFl)
    '''
    Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。 
        注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
    '''
    pool.close()#关闭进程池，不再接受新的进程
    pool.join()#主进程阻塞等待子进程的退出
    e2=time.time()
    print("并发执行时间",int(e2-e1),e2,e1)
    print(rl)
    