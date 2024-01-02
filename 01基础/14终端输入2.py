import argparse

parser=argparse.ArgumentParser('desc:程序处理')
parser.add_argument('number',type=int,default=10,help='数字')
args=parser.parse_args()
print(args.number)