# ⾃定义模块
# 创建⾃定义模块
# • 使⽤以 .py 为结尾的⽂件名保存模块
# • 在⽂件中定义的属性、函数都可以被调⽤
# • 在⽂件中定义的类可以在引⽤模块时进⾏实例化



# ⾃定义模块注意事项
# 1. 导⼊⾃定义模块时，需确保导⼊路径正确
# 2. ⾃定义模块的⽂件名称尽量避免特殊字符，⽂件名应避免和标准库重名
# 3. ⾃定义模块多次导⼊，模块中的代码也只能被执⾏⼀次
# 4. ⾃定义模块中应为函数定义，避免在模块中编写函数调⽤代码，或将函数
# 调⽤代码放在 __name__ 代码块中


# 总结
# ⾃定义模块使⽤以 .py 结尾的⽂件名作为模块的保存位置
# ⾃定义模块名称不应和标准库名称重名

# 在同级目录下 如果不在同一目录下 import是导入不了的
# import my
# my.fun1()



# 通过sys模块导入自定义模块的path
# 如果执行文件和模块不在同一目录，这时候直接import是找不到自定义模块的
# sys模块是python内置的，因此我们导入自定义模块的步骤如下：
# 先导入sys模块
# 然后通过sys.path.append(path) 函数来导入自定义模块所在的目录
# 导入自定义模块。
# from os import path as path_module
# from os import getcwd as current_working_directory
# print(current_working_directory())
# import sys 
# sys.path.append('/Users/yulang/Documents/地矿项目/other/pythonLearn')
# import my
# my.fun1()