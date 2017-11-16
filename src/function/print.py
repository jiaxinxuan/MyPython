'''
python 输出练习
英文文档：

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Print objects to the text stream file, separated by sep and followed by end. sep, end and file, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.

1. 用于对象打印输出。通过命名参数sep来确定多个输出对象的分隔符(默认' ')，
通过命名参数end确定输出结果的结尾(默认'\n')，通过命名参数file确定往哪里输出(默认sys.stdout)，通过命名参数fiush确定输出是否使用缓存(默认False)。
'''
import sys

#1.end参数练习

#默认输出，默认输出换行
print("1234");
#指定输出文字的结尾为end
print("1233",end="end");
#输出的结尾换行
print("输出结果换行",end="\n");
#输出的结尾不换行
print("输出的结果不换行",end="")
'''
总结：在print函数中，默认的end缺省值是"\n",即是换行符。可以指定任何至在结尾输出。例如：不想换行，指定结尾为"".
注意的是：输出的值取的是对象的地址，不用指定参数名称，直接输出即可。
'''
print("\n########sed参数练习#########")
#2.sed参数练习

#sep 参数指定是多个输出结果的情况，当有多个输出参数时，可以用sep指定他们之间的分隔符
print("1234","fefef",sep=",")
print("1","2","3","4",sep="\n",end="")
'''
此参数可以用于字符串输出的情况
'''
print("\n########file参数练习#########")
#3.file 参数练习

#此参数执行输出到那里，file参数必须是一个含有write(string) 方法的对象。，默认是sys.stout,即控制台

class A:
    @staticmethod
    def write(s):
        print(s)

a=A();
print(1,2,3,4,sep="|",end="=?",file=a)

'''
总结：print的输出和c语言的挺像，不过它是函数式编程语言，相较于Java还是比较难理解些。
'''


class jiaxinuan:

    #定义简单输出函数
    def wangbadang(self):
        str = ' 1223333';
        print(str);

jia=jiaxinuan();
jia.wangbadang();