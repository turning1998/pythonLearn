# ()内写继承的类,多个用逗号隔开
# 继承可以让新⼿快速上⼿⼤⽜设计的代码
# • ⽐如，你希望⾃⼰的类能够实现字典 + 额外功能，那么你可以使⽤如下代码实现：
#  from collections import UserDict
#  class my_dict(UserDict):
#  …
# class Person():
#   name=''
#   age=0
#   def add_sex(self):
#     self.sex='male'
#     pass

# class Student(Person):
#   grade=0
#   def add_grade(self):
#     self.grade=1
#     pass

# stu1=Student()
# stu1.name='Tom'
# stu1.age=18
# stu1.add_grade()
# stu1.add_sex()
# print(stu1.name,stu1.age,stu1.grade,stu1.sex)



# ⼦类继承⽗类的⽅法：增加（或减少）功能时可以使⽤ super() ⽅法
# 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# • 多重继承增加了继承的复杂度，应当减少多重继承的使⽤
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
# class Student(Person):
#   grade=0
#   def add_sex(self):
#    super().add_sex() #调用父类的add_sex方法
#   pass


# • 菱形继承时，Python 会按照 C3 算法（有向⽆环路图）按顺序遍历继承图
# • 通过类对象名称.__mro__ 可以查看继承顺序
# • 多重继承增加了继承的复杂度，应当减少多重继承的使⽤



#  通过类对象名称.__mro__ 可以查看继承顺序
# • 多重继承增加了继承的复杂度，应当减少多重继承的使⽤
# print(Student.__mro__)
# (<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)

# 混入
# 混⼊ Mix-In 是指借⽤多继承的语法，为现有类增加新的⽅法
# • 混⼊不定义新的属性，只包含⽅法
# • 混⼊便于重⽤，但绝不能实例化
# • 混⼊类⼀般在类名称后增加 Mixin
# 例如： 披萨可以按层数分为单层、双层，也可以按照形状分为圆形、⽅形，可以将它们定义为：单层Mixin、双层Mixin、圆形Mixin、⽅形Mixin

# 定义⼀个披萨类：
#  class 披萨(主要材料, 单层Mixin, 圆形Mixin)