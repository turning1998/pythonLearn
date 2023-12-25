# 1.不定长参数
#  *接收位置参数 【元组形式存储】
# **接收关键字参数【比如额外参数 不需要一一列举在函数参数里,以字典存储】
# 如果参数既有位置参数，又有关键字参数，位置参数必须在关键字参数前面[包括传递参数时]

# 混合定义时注意事项
# 参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
# def f1(a, b, c=0, *args, **kw):

# def testFun(a,*b,**c):
#   print(a,b,c)
# testFun(1,2,3,'a',99,name='Tom',age=20) 
# a=1 b=(2,3,'a',99) c={'name': 'Tom', 'age': 20}
# 错误写法 testFun(1,2,3,name='Tom',20,age=20) 20错误





#2.不定长参数的变种    有疑问*

# 只想取特定位置的参数
# *号之后没有变量名称，只处理第一个和最后一个，第二个参数忽略
# 注意：由于最后一个是关键字参数，所以参数长度被固定为3个

# def test1(a,*,b):
#   print(a,b)
# test1(1,b=2)




# 3函数文档--主要是描述函数的用途，用法，注意事项等
# def foo():

#     """
#     这是foo函数
#     """
#     print("foo")

# print(foo.__dir__)




# 函数返回值 return
# 如果函数内不定义 return 语句，或返回表达式为空，那么默认返回 None
# def foo():
#   # print('foo')
#   return 'foo'
# print(foo())

# RecursionError: maximum recursion depth exceeded
def func1():
 return 1
def func2():
 return func2()
result = func2()