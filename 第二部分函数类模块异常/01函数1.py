# 函数--重复 到处使用

# 1.定义
# def 函数名称([函数参数]):
#    函数体
#    [return 返回值]

# def foo():
#   print(11) 

# 2.调用
# def foo():
#   print(11) 
  
# foo()


# 3匿名函数

# add=lambda x,y:x+y  #传入 x和y,返回x+y
# print(add(1,2))


# 4函数的参数

# 实参和行参数

# def func(args): #args是形参
#   print(args)
  
# func('2') #‘2’是实参



# 函数类型提示
# def func(arg:int)->int:
#   print(arg)
#   return arg

# func('a')



# 位置参数

def foo (argv1,argv2,argv3):
  print(argv1,argv2,argv3)
  
# foo('1','2') #TypeError: foo() missing 1 required positional argument: 'argv3'
foo('2','3','2')