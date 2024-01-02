# 装饰器 函数嵌套的定义与调用的区别


# 变量作用域
# 函数内部定义的变量，函数外不可以访问
# 如果函数内外都定义同一个变量名字  依然搁置访问

# eg1:
# number=12
# def foo():
#   number=10
#   print(number)
# foo()
# print(number) #函数


# 变量作用域：
# https://segmentfault.com/a/1190000000640834

# LEGB规则：LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
# local 本地变量:是函数内的名字空间，包括局部变量和形参
# Enclosed 闭包变量 外部嵌套函数的名字空间（闭包中常见）
# Global 全局变量 函数定义所在模块的名字空间
# Builtin 内置变量 内置模块的名字空间

# 在 Python 中检索一个变量的时候，优先回到 locals 里面来检索，检索不到的情况下会检索 enclosing ，enclosing 没有则到 globals 全局变量里面检索，最后是到 builtins 里面来检索。

# 当然，因为 builtins 的特殊性，我们可以直接在 builtins 里面添加变量，这样就可以在任意模块中访问变量，不过这种方法太过于变态，不推荐这么做。



# # 闭包
# 函数内的再次定义的内部函数形成闭包
# • 闭包作⽤域之内，内部函数可以访问外部函数的变量
# def out():
#   number=10  #闭包变量
#   def inner():
#     return number*199
#   return inner

# print(out()())



#装饰器 https://zhuanlan.zhihu.com/p/39093542
# 可以让其他函数在不需要做任何代码变动的前提下增加额外功能；

# 装饰器的返回值也是一个函数对象。简单的说装饰器就是一个用来返回函数的函数。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
# 概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

# use_logging装饰器  把执行真正业务方法的func包裹在函数里面
# def use_logging(func):
#     print("%s is running" % func.__name__)
#     func()

# def bar():
#     print('i am bar')

# use_logging(bar)
# 运行结果:
#bar is running
#i am bar


# 装饰器语法糖
# python提供了@符号作为装饰器的语法糖，使我们更方便的应用装饰函数；但使用语法糖要求装饰函数必须return一个函数对象。因此我们将上面的func函数使用内嵌函数包裹并return。

# 装饰器相当于执行了装饰函数use_loggin后又返回被装饰函数bar,因此bar()被调用的时候相当于执行了两个函数。等价于use_logging(bar)() 。
# def use_logging(func):
#     def _deco():
#         print("%s is running" % func.__name__)
#         func()
#     return _deco

# @use_logging   #@+函数名称
# def bar():
#     print('i am bar')

# bar()


#eg2 计算函数运行时间

# import time
# def func():
#   print('开始')
#   time.sleep(1)
#   print('结束')

# start=time.time()
# func()
# stop=time.time()
# print('总共运行了%s秒' % (stop-start))

# 改写为@

# import time 
# def timeCount(fun):
#   def wrapper():
#     start=time.time()
#     fun()
#     stop=time.time()
    
#     print('总共运行了%s秒' % (stop-start))
#   return wrapper

# @timeCount
# def func():
#     print('开始')
#     time.sleep(1)
#     print('结束')

# func()



# ⾃带装饰器
# • Python 内置的装饰器使⽤了 functools 包
# • 常⽤的有：
#  @lrucache # 缓存
#  @wraps # 被装饰函数保持原对象不变

