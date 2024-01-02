str1 ='a'
str2="abc"
str3='''
xxxx
'''

str4='test'
print(str1)
print(str2)
print(str3)
print(f"{str4}:{str1}")

x in str 
# x子串是包含在str  True False
x not in str
#x子串没有包含在str中 True False
str.count() 出现次数
str.isalnum() 字符串是否只有字母和数字组成
str.isalpha() 字符串是否都是字母组成
str.join(val) 字符串遍历val的值和str每次做拼接
str.split() str内字符由什么进行分割 不能是空
str.startswith() 字符串是以什么开头的
str.endswith() 字符串是以什么结尾