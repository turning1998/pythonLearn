# 标准库中的所有组件⽬录：
# https://docs.python.org/zh-cn/3.10/library/index.html
# 内置函数、类型、异常
# ⽂本处理
# 数字
# ⽂件和⽬录
# 通⽤操作系统
#  并发执⾏ ⽹络和进程间通信 互联⽹协议  


# 需求：
# 通过 Python 模拟浏览器访问 http://www.baidu.com
# 实现步骤：
# 1. 通过官⽅⽂档找到互联⽹协议和⽀持
# 2. 找到 HTTP、urllib ⽬录参考
# 3. 最终确定 urllib.request 可以实现相应功能
# 4. 参考⽂档中的“例⼦”和 urlopen() 函数的参数说明，实现模拟浏览器的⽬的
# * 官⽅⽂档：
# https://docs.python.org/zh-cn/3.10/library/urllib.request.html#examples

# import webbrowser
# url = 'http://www.baidu.com'
# webbrowser.open(url)

# import requests

# url = 'http://www.baidu.com'

# response = requests.get(url)

# print(response.text)

# 标准库能⽀持各种扩展功能，并提⾼ Python 的开发效率
# 标准库中的包⾮常多，不必逐⼀使⽤和熟练掌握，掌握⽂档的查阅⽅法即可