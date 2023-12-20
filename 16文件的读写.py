# 文件的写入

fileReader=open("test.txt","w")
fileReader.write('hello 2023')
fileReader.close()

# 文件的读取
fileReader=open("test.txt","r")
res= fileReader.readline()
print(res)
fileReader.close()