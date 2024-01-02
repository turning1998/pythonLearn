# 定义类
# 首字母大写
class Person:
   name=''
   age=0
   def add_sex(self):
     self.sex='male'
     

p1=Person() #实例化

print(p1.age) #0
p1.add_sex()
print(p1.sex) #male
  