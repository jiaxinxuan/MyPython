'''
py语法练习
@author: Administrator
'''
#第一例
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排序

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and b!=c and a!=c:
                print(a,b,c)
#第二例

题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

arr=[1000000,600000,400000,200000,100000,0];
ait=[0.01,0.015,0.03,0.05,0.075,0.1]
# while 1:
# i=int(input("请输入当月奖金："))
# r=0
# for idx in range(0,6):
#     if arr[idx]<i :
#        r+=(i-arr[idx])*ait[idx]
#        print (r)
#        i=arr[idx]
# print("奖金结果:",r)
#第三例

题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
x+100=n2,x+100+168=m2
m2-n2=168=(m+n)(m-n)
i=m+n,j=m-n
i*j=168 ----->168是j的整数倍，168%j==0
m=(i+j)/2   m,n为整数，则(i-j)%2==0，(i+j)%2==0
n=(i-j)/2   ---->i大于j,i>j

for i in range(1,85):
    if(168%i==0):
        j=168/i;
        if i*j==168 and (i-j)%2==0 and (i+j)%2==0 :
            m=(i+j)/2
            n=(i-j)/2 
            x=int(n*n-100)
            print(x)
#第四例

题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

days=[31,29,31,30,31,30,31,31,30,31,30,31];
year=int(input("year:"))
mouth=int(input("mouth:"))
day=int(input("day:"))
tatal=0;
for num in range(0,mouth):
    if(mouth==1):
        tatal=0
    else:
        tatal+=days[num-1]
if not((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    tatal=tatal-1;
print("总的天数：",tatal+day)
print(year%100)
#第五例
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
利用Python的列表，比较好解决这种问题！！！！！
list=[]
for i in range(3):
    list.append(int(input("integer:\n")))
list.sort
print(list)
print(list.pop())
#第六例
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)

打印给定整数内的数列

#求数列的递归求法，指定某一位
def Fibonacci(num):
    if num==1 or num==2:
        return 1
    elif num==0:
        return 0 
    elif num>=2:
        return Fibonacci(num-1)+Fibonacci(num-2)
#求指定个数的数列
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])#fibs[-1]表示取列表的倒数第一个值
    return fibs
 
# 输出前 10 个斐波那契数列
print (fib(10))
第七例
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。

list1=[1,2,3,4,5,6,7,8,9]
list2=[]
for num in list1:
    list2.append(num)
print(list2)
list2=list1[:]#此处为截取列表的全部，然后赋值给list2
print(list2)
list3=list1.copy()
print(list3)
import copy
list4=copy.copy(list1)
print(list4)
#第八例
打印九九乘法口诀
'''

from _ast import Num


for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t" % (i,j,i*j),end=" ")
    print()
