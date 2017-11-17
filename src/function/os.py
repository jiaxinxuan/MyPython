import os
import os.path
import sys

"""
获取指定目录及其子目录下的 py 文件路径说明：list 用于存储找到的 py 文件路径 get_file 函数，递归查找并存储 xml 文件名称
"""

list = []


def get_file(path, list):
    if os.path.isdir(path):
        file_list = os.listdir(path)
        try:
            for file in file_list:
                file_temp = os.path.join(path, file)
                if os.path.isdir(file_temp):
                        get_file(file_temp,list)
                else:
                    if file.endswith("xml"):
                        list.append(os.path.join(path, file))
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


path = input("请输入路径:")

get_file(path, list)
print("xml文件个数:", list.__len__())
for file in list:
    print(file, end="\n")

