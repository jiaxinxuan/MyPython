#!/usr/bin/python
from _ast import If
import sys


#Python输出语句练习
x="a"
y="b"
# 换行输出
print (x)
print (y)
print ('---------')
# 不换行输�?
print(x,end=" ")
print(y,end=" ")
#�?行输出多个变�?
print(x,y,x,y,":此行有多个�?�输�?")
#for循环语句
for num in range(10):
    print(num,end="")
#Python变量练习
"""
python在定义变量时，必须初始化，否则虚拟机不予分配空间。变量根据实际赋值来决定是何类型
"""
miles=32.000
integer=123
varchar="adaffaaf"
print(miles,integer,varchar);
#1变量赋�??
a=b=c=1;
print(a,b,c)#创建�?个整型对象，值为1，三个变量被分配到相同的内存空间上�??
#2变量赋�??
del a,b,c;#删除对象的引用，
a,b,c=1,2,"abc"#多个对象指定多个变量，给对象重新赋�??
print(a,b,c)
#字符串练�?
str="abcdefglove"
print("字符串练习！")
print(str)#输出全部的字符串
print(str[2])
print(str[0:1])#输出的�?�是a
print(str[3:5])#输出的�?�de
print(str[3:])#从下标为三的字符�?始直到最后一个字�?
print(str*2)#连续两次输出该字符串

#Python列表练习
#列表中可以存储各种标准数据类�?
#列表的定义方式类 变量�?=["","",,];
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第�?个元�?
print (list[1:3])          # 输出第二个至第三个的元素 
print (list[2:])           # 输出从第三个�?始至列表末尾的所有元�?
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列�?
list.append("贾新�?")
print(list[list.__len__()-1])#输出�?后列表中的最后一个�??

#python 元组练习
'''
python 中的元组，一经赋值就不可再改变，相当于只读列表，其余则和列表很像，定义方式，元组=�?"",""�?
'''
tuple=("jia","xin","xuan",1,2,3)
print(tuple)
print(tuple[0],tuple[1],tuple[2])
sys.stdout.write(tuple[0]+tuple[1]+tuple[2])#引用sys模块，使输出无空�?

#Python字典练习
'''
字典(dictionary)是除列表以外python之中�?灵活的内置数据结构类型�?�列表是有序的对象结合，字典是无序的对象集合�?
两�?�之间的区别在于：字典当中的元素是�?�过键来存取的，而不是�?�过偏移存取�?
字典�?"{ }"标识。字典由索引(key)和它对应的�?�value组成�?
字典和Java中的map差不多，也和json差不多，都是键�?�对映射的关�?
'''
print("\n字典练习")
dict={"1":"�?  ","2":"�?","3":"�?"}
print(dict.keys())
print(dict.values())
print(dict["1"]+dict["2"],dict["3"])
dict={"34":"wangbadan","21":"我是你大�?","贾新�?":123}#这个地方相当于重新对这个对象赋�?�，�?以上面的值都丢失�?
print(dict)
print(dict["贾新�?"])
print(dict.keys())
print(dict.values())

#python 的算术算术运算符
a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的�?�为�?", c)
 
c = a - b
print ("2 - c 的�?�为�?", c) 
 
c = a * b
print ("3 - c 的�?�为�?", c) 
 
c = a / b
print ("4 - c 的�?�为�?", c) 
 
c = a % b
print ("5 - c 的�?�为�?", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print ("6 - c 的�?�为�?", c)
 
a = 10
b = 5
c = a//b 
print ("7 - c 的�?�为�?", c)

#python 比较运算�?
a = 21
b = 10
c = 0
 
if ( a == b ):
   print ("1 - a 等于 b")
else:
   print ("1 - a 不等�? b")
 
if ( a != b ):
   print ("2 - a 不等�? b")
else:
   print ("2 - a 等于 b")
 
if ( a < b ):
   print ("4 - a 小于 b") 
else:
   print ("4 - a 大于等于 b")
 
if ( a > b ):
   print ("5 - a 大于 b")
else:
   print ("5 - a 小于等于 b")
   
#python的成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if (a in list):
    print("a-在list里面");
else:
    print("a-不在list里面");
if(b not in list):
    print("b-不在list里面")
else:
    print("b-在list里面")
 
# 修改变量 a 的�??
a = 2
if (a in list):
    print("a-在list里面");
else:
    print("a-不在list里面");
# 改变b的�??
b=2
if(b not in list):
    print("b-不在list里面")
else:
    print("b-在list里面")
    
#Python身份运算�?
obj1=obj2=123

if(obj1 is obj2):
    print("obj1和obj2引用同一个对�?")
else:
    print("obj1和obj2不是引用同一个对�?")
#改变两�?�的引用对象
obj2="4567"
if(obj1 is not obj2):
    print("obj1和obj2不是引用同一个对�?")
else:
    print("obj1和obj2引用同一个对�?")
'''
is �? == 区别�?
is 用于判断两个变量引用对象是否为同�?个， == 用于判断引用变量的�?�是否相�?
'''
#python的条件语�?
str1="123"
str2="123"

if str1==str2:
    print("str1和str2相等")
else:
    print("str1和str2不相�?")
    
if (str1==str2):
    print("str1和str2相等")
else:
    print("str1和str2不相�?")
    
num=5
if(num==1):
    print("老板好！")
elif(num==2):
    print("老板娘好�?")
elif(num==4):
    print("经理好！")
elif(num==5):
    a=1; b=2;a=a+b;
    print("您好啊！",a)
else:
    print("您真的太好了�?")

#python的循环语�?
num=0;
i=5
while i>=0:
    num=num+i
    i-=1
print("累加和为�?",num)

list=[1,2,3,4,5,6,7,8,9]
even=[]
add=[]
while(len(list)>0):
    number=list.pop()#这个仿佛是从栈顶取�??
    if(number%2==0):
        even.append(number)
        if(number==8):
            break
    else:
        add.append(number)
print(even,"这里是偶�?")
print(add,"这里是奇�?")
#Python的for循环
for letter in 'Python':     # 第一个实�?
   print ('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实�?
   print ('当前水果 :', fruit)
 
print ("Good bye!")