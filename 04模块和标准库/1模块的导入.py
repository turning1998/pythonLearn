# 模块 是存放了函数的且以.py结尾的文件
# 将函数放在模块文件里 ，有助于隐藏代码细节，使程序的主要逻辑更清晰

# 导入整个模块 
# import os

# 导入模块特定函数  要注意和编写的其他函数名不要冲突
# from os import path
# from os import chdir,getcwd
# 导入模块特定函数并重命名
# from os import path as path_module
# from os import getcwd as current_working_directory
# print(current_working_directory())


# 导入包
# 多个模块放在一个文件夹内，改文件夹称作为包
# 包的导入与模块的导入相同：
# import 包 或 from 包 import 模块
# import numpy as np
# 导入子包
# 子包的导入与包的导入相同：
# import 包.子包 或 from 包.

# 不同方式
# import os
# os.getcwd()
# 推荐使用
# from os import getcwd
# getcwd()