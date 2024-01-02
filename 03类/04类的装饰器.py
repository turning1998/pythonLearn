# 类的装饰器 改变类的方法的功能



# classmethod装饰器 类的装饰器是类的方法的装饰器的缩写-方法
# 可以通过装饰器改变方法的调用方式和行为
# classmethod可以实例的方法定义为类的方法，用于类直接调用
class Klass:
  @classmethod
  def func(cls):   #cls表示当前操作的类 
    print("this is a class method")
Klass.func()  #直接定义不用再实例化



# staticmethod装饰器 静态方法--方法
# 不需要类的任何信息但⼜和类相关的⼀些⽅法，为了⽅便维护代码并保持代码⼯整，
#  可以将该函数定义到类中并使⽤ staticmethod 修饰
# staticmethod 修饰的⽅法，不需要使⽤ self 或 cls

class Person:
  @staticmethod
  
  def func():
    print('xxx')
  pass




# property装饰器 属性装饰器 改变属性
# 把方法装饰成属性 把属性改成函数逻辑
class Student:
  @peoperty
  # 读取属性
  def func(self):
    return self.__varName
  @func.setter
  def func(self, value):
    self.__varName = value
  @func.deleter
  def func(self):
    del self.__varName


# 避坑指南：类的常⻅错误



# 语法错误：导致使⽤异常 
# 忘记使⽤ self 关键字
# 错误使⽤ self 与 cls 关键字



# 设计错误：导致耦合严重，⽆法拆分
# 设计错误
# • 哪些对象应该被抽象为类？
# • 哪些功能应该被定义为属性，哪些应该被定义为⽅法？
# • 如何解决类之间的依赖？



# 设计错误
# SOLID 原则：
# ‣ S 单⼀职责原则
# ‣ O 开闭原则
# ‣ L ⾥⽒替换原则
# ‣ I 接⼝隔离原则
# ‣ D 依赖倒置原则
# 单⼀职责原则：
# • 类只负责做⼀件事，即只有⼀个职责。即：越⼩越好
# 开闭原则：
# • 类应当对扩展开放，对修改关闭，使其有更好的可维护性
# ⾥⽒替换原则：
# • 某个对象使⽤类的⼦类时，应当和使⽤⽗类有相同的⾏为。
# •即：对于任何类，客户端都能应该能⽆差别的使⽤它的⼦
# 类，并且不会影响运⾏时的预期⾏为。
# 接⼝隔离原则：
# • Python 使⽤“鸭⼦类型”实现接⼝，接⼝越⼩越好
# 依赖倒置原则：
# • ⾼层模块不应该依赖低层模块，⽽是应该让⼆者依赖抽象


# 总结
# self 是刚开始学习⾯向对象编程时，最容易忽略的语法
# 编写多个类时，解决依赖关系是初学者最难把握的部分，使⽤ SOLID 指导原则，
# 可以有效拆分类

# init⽅法
# • __init__() 称作初始化⽅法，⽤于属性和⽅法初始化⽅法
# • 在类实例化时⾃动进⾏初始化
# • 初始化⽅法还可以让类实例化时接收参数
# class Klass:
#  def __init__(self, 接收参数)
#  self.var = 参数
# 实例 = Klass( 参数 )