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
