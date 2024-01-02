# ，一个程序如果使用文件作为输入系统要考虑的三件事：文件是否存在，文件是否有可读权限，使用正确的文件编码。
# 1.文件是否存在
f = open("c:\\a.txt")

# 错误提示
# Traceback (most recent call last):
#   File "d:\temp\a.py", line 1, in <module>
#     f = open("c:\\a.txt")
#         ^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'c:\\a.txt'

f = open("c:\\windows")  # 打开一个文件夹

# 错误提示
# Traceback (most recent call last):
#   File "d:\temp\a.py", line 1, in <module>
#     f = open("c:\\windows")
#         ^^^^^^^^^^^^^^^^^^^
# PermissionError: [Errno 13] Permission denied: 'c:\\windows'
# 我使用 open() 函数打开了 windows 文件夹，由于 Python 判断文件的内部逻辑优先判断权限，因此它告知开发者，你打开的文件权限不足，而根本原因是打开了一个文件夹。报错的提示并不是根本原因，自然无从下手解决问题了。

# 除了 Python 报告的异常不准确外，还有一个更严重的问题，就是它的异常提示信息对非开发人员来说不够友好，用户使用你的程序时，你应当告知用户如何正确使用你的程序，而不是将程序执行引发的异常直接告诉最终用户。

# 所以正确的做法是，在打开文件之前，判断文件存在且操作的指定路径是一个普通文件。在 Python 中，这一操作可以通过 Python 的标准库直接实现。我把判断文件的代码写在下面，你可以直接拿到程序中使用。
import pathlib
import sys

path = pathlib.Path("d:\\ab.txt")
if path.is_file():
   print(f"{path} 是文件")
else:
   print(f"{path} 不是文件, 请重新创建文件")
   # 退出程序
   sys.exit(1)
# 以上代码中，我使用了 pathlib 库中的 is_file() 函数判断 Path 引用的路径是否为文件，如果为文件的话返回值为“True”，否则为“False”。这段代码的第 5 行你要注意，不要使用“if path.is_file() == True”的写法画蛇添足，Python 的条件语句能根据 is_file() 函数返回值，进行分支语句判断。
# 看完了文件是否存在的判断，我再来带你学习一下如何判断是否有文件的读取权限。




# 2. 文件是否有可读取权限

# 如果你不判断文件的读取权限，一旦程序读取到没有权限访问的文件时，会提示你 PermissionError 异常。为了程序执行过程更加流畅，我们在判断文件存在之后，往往会继续判断要操作的文件是否有必需的文件权限。这一操作，要借助 os 库来实现，我将它的判断方法写在下面供你参考。

# 复制代码
# import pathlib
# import os
 
# path = pathlib.Path("d:\\a.txt")
 
# if os.access(path, os.R_OK):
#     print("文件可以读取")
 
# if os.access(path, os.W_OK):
#     print("文件可以写入")
# 代码中，我借助 os 库的 access() 函数，实现了对文件权限的判断，它的第一个参数是要判断权限的文件路径，第二个参数是判断权限的标准，其中 R_OK 用来判断文件读取权限，W_OK 用来判断文件写入权限。
# 正确的权限可以确保文件能够被读取，而文件中的内容能否正确呈现，则要看你是否使用了正确的文件编码。




# 3. 正确的文件编码

# 文件编码问题，长期困扰着 Python 开发的初学者，很多同学甚至为了研究透编码的定义和转换，下了一番苦功。其实编码问题对于日常开发来说，比你想的要简单，当你遇到编码和当前系统不一致的问题时，不需要通过各种复杂代码进行编码的转换，你只要“按照文件保存时指定的编码打开”即可。

# 即你使用的是 Windows 默认采用“GBK”编码，如果你要打开 macOS 系统编写的“UTF-8”编码的文件，你只需要将 open() 函数的 encoding 参数指定为“encoding=UTF8”，文件就能按照正确的编码识别文件了。切记不要再进行复杂的编码转换了，不然容易导致更多字符集不兼容问题。

# 如果你也和我一样经常使用 Windows 和 macOS 两个平台的话，可以参考下面代码，可以判断文件编码。

# 复制代码
# # pip3 install chardet
# # chardet 是第三方库，需要通过 pip 命令为 Python 安装后使用
 
# from chardet.universaldetector import UniversalDetector
 
# detector = UniversalDetector()
 
# with open("d:\\temp\\a.txt", "rb") as f:
#     detector.feed(f.read())
#     detector.close()
 
#     print(detector.result)
# # {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
# 以上代码，对文件进行判断之后，通过 detector.result 得到一个字典，其中字典 encoding 键对应的值就是文件的编码，我将这段代码运行在 Windows 上面，如果文件为 utf-8 编码，打开文件时在 open() 函数中增加 encoding=utf8 参数，否则不加。

# 从上面三个例子我们知道，要使用文件作为一个程序的输入并不简单，但是只要考虑三个重要的事情，大部分场景你都能应对自如。它们分别是，打开文件前应判断文件是否存在，否则会出现异常。文件存在也无法访问，是因为文件权限设置不当。文件存在但是读取内容错误，是因为文件编码不正确。

# 输出
# 除了使用文件作为输入要考虑三件事外，使用文件作为输出时，你也要考虑两件事：文件要保存的文件夹是否存在；如果文件夹不存在，你要如何创建文件夹。

# 下面就是判断文件夹是否存在的代码，我来讲解一下。

# 复制代码
# import pathlib
# import sys
# import os
 
# dir = "d:\\dir1\\dir2"
# path = pathlib.Path(dir)
# if path.is_dir():
#     print(f"{path} 文件夹存在")
 
# else:
#     print(f"文件夹不存在，创建{path} 文件夹")
 
#     # 创建多级文件夹
#     os.makedirs(dir)
# 以上代码实现了判断文件夹是否存在，如果不存在的话自动创建多级文件夹操作。

# 上面代码的第 7 行和第 14 行需要你特别注意，其中第 7 行实现了对文件夹类型的判断。第 14 行使用了 os 库的 makedirs() 函数创建多级文件夹。os 库创建文件夹有两个函数，分别为 mkdir() 和 makedirs() ，前者可以创建一级文件夹，后者可以创建多级文件夹。当你需要创建文件夹时，可以根据不同的需求使用不同的函数。

# 小结
# 以上就是今天我分享的，在输入和输出的时候，使用文件作为操作对象的注意事项。我将出现异常报错，改造成操作前要确认路径、权限和字符编码，也就是代码运行前，检查所有必须满足的条件，如果不满足就先告知用户错误。

# 这种做法被称作契约式编程结构中的前置条件检测。与其在代码运行中抛出异常，不如和程序的调用者达成契约，一旦违反契约 (文件无法创建、读写)，就明确指出无法继续下去的原因。

# 契约式编程结构让你的程序更加健壮，而且有助于你更好地阐明程序的结构。
