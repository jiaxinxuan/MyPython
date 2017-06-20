'''
Created on 2017年6月20日

@author: Administrator
'''
import jieba
'''
练习使用结巴分词，顺便练习下文件的读写
'''
def sliptsentence(inputFile,outPutFile):
    try:
        inFile=open(file=inputFile, mode="r",encoding="UTF-8")#以读的方式打开该文件
        outFile=open(file=outPutFile,mode="w",encoding="UTF-8")#以写的方式打开该文件
        '''
                循环遍历打开的文件，取出其中每行，并对每行进行分词
        '''
        for eachLine in inFile:
            line=eachLine.strip().encode("UTF-8","ingore")#此句取某一行的数据，并且去除两端的空格，并以utf-8的形式编码
            wordList=jieba.cut(line);
            '''
                        将当前行得到的分词数据，写入到输出文件中去
            '''
            outstr=''
            for word in wordList:
                outstr+=word
                outstr+="/"
            outFile.write(outstr.strip()+"\n")
    except :
        print("文件处理出错")
    finally:
       inFile.close()
       outFile.close() 
sliptsentence(r"F:\test.html", r"F:\test.txt")