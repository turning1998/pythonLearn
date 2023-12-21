# 1. 百分号%输出
# a=int(input("请输入一个数字1:"))
# b=int(input("请输入一个数字2:"))
# a = 1
# b = 2
# print('%s is %s', %(1, 2))

# 2.format()函数

# print("{1} is {0}".format(1, 2))  // 2 is 1


# 3f-string(一般使用) ( python3.6以上版本推出)

# a=2 
# b=3
# print(f"{a} is { b}")  # 2 is 3

# f-string 实现数据计算 字符串拼接 函数执行

print(f"{1+2}")  #3
print(f"{'a'+'b'}") # ab
f"{print('c')}"   #c

# f-string 宽度和精度的调整
number=10000
print(f"{number:6}") # _10000 （前面有一个空格）

number1=123.456
print(f"{number1:10}")  #_ _ _ 123.456 (前面有3个空格)
print(f"{number1:-10}")  #123.456_ _ _ (后面有3个空格)

print(f"{number1:010}") #000123.456 (前面有3个0)

print(f"{number1:.4f}") #指定类型f:浮点数 123.4560
print(f"{number1:4f}") #指定类型f:浮点数 123.456000