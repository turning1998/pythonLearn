# 合并文件 =读取原始文件+追加写入新的文件
# 打开a.txt,b.txt,合并生成c.txt
# 1.打开原始文件
# 2.写入模式创建并打开要合并的文件
# 关闭文件 
 
with open('a.txt') as f1, open('b.txt') as f2:
  content1=f1.read()
  content2=f2.read()

# print(content1,content2)

with open('c.txt','w') as f3:
  f3.write(content1+' '+content2)
  
