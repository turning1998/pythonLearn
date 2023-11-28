# 导入
with open('./6demo.csv') as f:
  file_data = f.readlines()
# 用tinydb存储数据 安装 pip3 install tinydb
from tinydb import TinyDB, Query
db=TinyDB('./6.json')
listdb=[]
for row in file_data:
   listdb.append({
       'index':row.split(',')[0],
       'name':row.split(',')[1],
       'source':row.split(',')[2],
       'tel':row.split(',')[3].strip()
   })
db.insert_multiple(listdb)
# print(db.all())
query1=Query()
friend_info=db.search(query1.name == '张三1')
print(f"名字是{friend_info[0]['source']}")