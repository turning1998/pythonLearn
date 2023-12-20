# 文件的写入

# fileReader=open("test.txt","w")
# fileReader.write('hello 2023')
# fileReader.close()

# 文件的读取
# fileReader=open("test.txt","r")
# res2=fileReader.read() 
# print(res2)
# fileReader.close()

# fileReader=open("test.txt","r")
# for i in fileReader:
#   print(i)
string1 = """Python 3.11 is up to 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite. See Faster CPython for details. """
fileWirte =open('a.txt','w')
fileWirte.write(string1)
fileWirte.close()

fileReader2=open("a.txt","r")
content =fileReader2.read()
print(content)
fileReader2.close()
fileWrite3=open('b.txt','w')
fileWrite3.write(content)