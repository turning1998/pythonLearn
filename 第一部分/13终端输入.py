# argparse

import argparse
parser=argparse.ArgumentParser(description='This is a description')
# 可选参数 -number
# parser.add_argument('-number',help='输入一个数字')
# args=parser.parse_args()
# print(f"你输入的参数是{args.number}")
# python3 13文件.py  -number 100 运行



# 必选参数 number
parser.add_argument('number',help='输入一个数字')

args=parser.parse_args()
print(f"你输入的参数是{args.number}")

#  python3 13文件.py 
# 13文件.py: error: the following arguments are required: number

#   python3 13文件.py   100 
# python3 13文件.py   100       

# python3 13文件.py   --help
