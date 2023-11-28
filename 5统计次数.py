

# 统计单词i出现的次数
# 统计单词you和You出现的次数

import pprint
with open('./5demo.txt') as f:
  file_data = f.readlines()
  pprint.pprint(file_data)
#  统计文件行数
# print(len(file_data))
# # 统计不包括空行的行数
# for  x in file_data:
#   if x.strip() == '':
#     del file_data[file_data.index(x)]

# print(len(file_data))

# print(len(file_data )- file_data.count('\n'))
# print(len(set(file_data))-1)
print(str(file_data))
print(str(file_data).split(' ').count('you'))
