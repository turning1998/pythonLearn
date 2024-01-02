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
# print(list(res)) # [2, 4, 6, 8, 10] #map转为list

# 基本用法
# 可以在function处使用匿名函数lambda：
# res=map(lambda x:x*2, [1, 2, 3, 4, 5])
# map函数还可以用来进行类型转换
# print(list(map(int,(1,2,3)))) #[1,2,3]
# print(list(map(int,'123'))) #[1,2,3]
# print(list(map(int,{'1':2,'2':3,'3':4}))) #[1,2,3]



# filter()
# filter(函数，可迭代对象)
# 函数：函数对象，lambda表达式
# 可迭代对象：列表/元组/range等
# 过滤掉可迭代对象中返回值不为True的元素
# filter函数返回一个可迭代对象
# res=filter(lambda x:x>3, [1, 2, 3, 4, 5])
# print(res) #<filter object at 0x7fbd48b3f490> 迭代器
# print(list(res)) #[4,5]



# reduce()
# reduce(函数，可迭代对象)
# 函数：函数对象，lambda表达式
# 可迭代对象：列表/元组/range等
# 对可迭代对象进行累积

# from functools import reduce
# res=reduce(lambda x,y:x+y, [1, 2, 3, 4, 5])
# print(res) #15


# 偏函数 固定某个参数，形成新的函数【通过固定旧函数的参数形成新的参数】
# 
from functools import partial
def mod( n, m ):
  return n + m
 
mod_by_100 = partial( mod, 100 ) # 固定了参数100，又不影响函数的定义
print(mod_by_100( 7 ))  # 107
print(mod_by_100( 9))  #109






