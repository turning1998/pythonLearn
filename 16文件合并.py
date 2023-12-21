# 合并文件 =读取原始文件+追加写入新的文件
# 打开a.txt,b.txt,合并生成c.txt
# 1.打开原始文件
# 2.写入模式创建并打开要合并的文件
# 关闭文件 
 
# with open('a.txt') as f1, open('b.txt') as f2:
#   content1=f1.read()
#   content2=f2.read()


# with open('c.txt','w') as f3:
#   f3.write(content1+' '+content2)

# 合并多个文件  遍历文件
# 1.将多个文件的文件名写入列表
# 遍历 列表
# 重构文件读写代码
# 将 a.txt, b.txt,c.txt重新写入d
fileName=['a.txt','b.txt','c.txt']
content=''
for  sigleFile in fileName:
    with open(sigleFile) as f:
      content+=f.read()
      
print(content)

with open('d.txt','w') as f12:
  f12.write(content)
