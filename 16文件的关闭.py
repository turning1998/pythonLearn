# 文件的关闭
# 读和写都建议关闭文件
# open()失败，不必close() 这里需要异常判断

# close
f1=open('text.txt',mode='r')
data=f1.read()
print(data)
f1.close()
# with语句
with open("test.txt", "r") as f:
   data=f.read()

print(data)
  