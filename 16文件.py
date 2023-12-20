# 文件  打开 关闭 读写 写入

#   打开-open()函数
#  open(filename,mode='r',buffering=-1,encording=None,errors=None,newline=None,closefd=True,opener=None)
#  mode='r' 只读 ,encoding='utf-8'
# fileTxt=open('./6demo.csv',mode='r',encoding='utf-8')
# print(fileTxt)

# 文件路径处理 打开的文件不在当前目录下
# 绝对路径方式
# fileTxt1=open('/etc/passwd')
# print(fileTxt1)

# 改变当前路径方式
# import os
# os.chdir('/etc') #改变当前路径
# fileTxt2= open('./passwd')
# print(fileTxt2)



# 文件编码
# windows 默认使用gbk
# linux/macos 默认使用utf-8
# open(fileName,encoding=UTF-8)
# open(fileNae,)encoding='gbk'