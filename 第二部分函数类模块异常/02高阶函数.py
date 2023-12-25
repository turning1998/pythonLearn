# 函数对象与函数定义
# def foo():
#   print('foo')
# foo() #函数调用
# f=foo  #函数定义
# f()





# map()
# map(函数，可迭代对象)
# 函数：函数对象，lambda表达式
# 可迭代对象：列表/元组/range等
# 将可迭代对象的每个元素作为函数参数执行
# def add(number):
#   return number*2
# # res=map(add, [1, 2, 3, 4, 5])  
# # 可以写为 
# res=map(lambda x:x*2, [1, 2, 3, 4, 5])


# print(res)  # 返回迭代器
# print(list(res)) # [2, 4, 6, 8, 10]

# 基本用法
# 可以在function处使用匿名函数lambda：
# res=map(lambda x:x*2, [1, 2, 3, 4, 5])
# map函数还可以用来进行类型转换
print(list(map(int,(1,2,3)))) #[1,2,3]
print(list(map(int,'123'))) #[1,2,3]
print(list(map(int,{'1':2,'2':3,'3':4}))) #[1,2,3]

