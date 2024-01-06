# 第三⽅模块的安装
# • 安装第三⽅模块使⽤ pip 命令
# pip3.10 install —— 第三⽅模块名称
# python3.10 -m pip install —— 第三⽅模块名称
# * https://pypi.org/project/requests/

# pip install requests 
# 或者 python3  -m pip install requests



# 不同程序要求的python版本不一样
# 虚拟环境
# 虚拟环境的⽤途：
# • 解决多个模块依赖的问题
# • ⼀次性安装多个指定版本的模块
# • 避免对默认环境造成污染
# 创建虚拟环境：
# python -m venv myvenv 【执行后目录下多了myvenv】下面是虚拟环境python的包


# • venv 虚拟环境模块
# • myvenv 保存虚拟环境的⽂件夹
# 将当前安装的包及其版本保存到⽂件中：
# pip3.10 freeze 【查看当前的文件包】
# pip3.10 freeze > requirements.txt 【保存到⽂件中】
# • 激活虚拟环境：
# source myvenv/bin/activate 

# • 在虚拟环境中导⼊指定的包：
# pip3.10 install -r requirements.txt

# • 离开虚拟环境：
# deactivate


# 加速第三⽅模块安装
# • 临时加速
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package_name
# • 永久加速

# cat ~/pip.conf
# [global]
# index-url = http://mirrors.aliyun.com/pypi/simple/
# [install]
# trusted-host=mirrors.aliyun.com
# 总结
# 第三⽅模块使⽤ pip 命令进⾏安装
# 为了避免污染默认环境，应尽量使⽤虚拟环境安装第三⽅模块
# 由于 pip 默认使⽤国外的源，下载安装包会出现超时的问题，可以通过
# 参数 -i 或修改配置⽂件加速下载过程


# python的虚拟环境是指一个隔离的Python运行环境，它可以包含不同版本的Python库和依赖项。虚拟环境可以帮助开发者安装和管理特定的库和工具，而不会影响系统默认的Python环境。

# 虚拟环境的工作原理是创建一个新的Python虚拟目录，并在其中复制或安装Python库。这样，在虚拟环境中安装的库就不会影响到系统默认的Python环境。开发者可以在虚拟环境中安装不同版本的库，例如Python 2.x和Python 3.x，或者安装特定于项目的库。

# 使用虚拟环境可以确保项目的依赖项不会影响其他项目或系统默认的Python环境。此外，虚拟环境可以确保项目的运行环境一致，即使在不同计算机上运行项目，也可以使用相同的虚拟环境。

# 要创建虚拟环境，可以使用venv模块。以下是一些常用的venv命令：

# 创建一个新的虚拟环境：python -m venv myenv
# 激活虚拟环境：source myenv/bin/activate（在Windows上使用myenv\Scripts\activate）
# 退出虚拟环境：deactivate
# 在激活虚拟环境后，可以使用pip命令安装库。例如，要安装requests库，可以运行以下命令：

# pip install requests
# 这将在虚拟环境中安装requests库，而不会影响系统默认的Python环境。

