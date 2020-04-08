class User1:
	def __init__(self,password):
		if len(password)>=6:
			self._password=password
		else:
			print("you have inputed the wrong length of password")

	def __str__(self):
		return "the password is %s"%self._password



class Animal:
	def __init__(self):
		self.name="xiaobai"
	def eat(self):
		print("eat something")
	def sleep(self):
		print("sleep")

class Dog(Animal):
	def shout(self):
		print("dog shout")
class Cat(Animal):
	def catchRat(self):	
		print("catch rat")



class Animal:
	def __init__(self):
		self.color="xiaobai"
	def eat(self):
		print("eat something")
	def sleep(self):
		print("sleep")

class Dog(Animal):
	def __init__(self,name):
		super().__init__()#active to use fathers Attribute
		self.name=name
	def shout(self):
		print("dog shout")
class Cat(Animal):
	def __init__(self):
		print("ready initiated")
	def catchRat(self):	
		print("catch rat")

#print(cat.name)
class BigDog(Dog):
 	def fight(self):
 		print("Bigdog to fight")
za=Dog("NiCai")
print(za.name)
print(za.color)


# Duck Sort of Python
class F1:
	def show(self):
		print(F1.show)
class S1(F1):
	def show(self):
		print(S1.show)
class S2(S1):
	def show(self):
		print(S2.show)
def Func(obj):
	print (obj.show())
s1_obj=S1()
Func(s1_obj)
s2_obj=S2()
Func(s2_obj)	
 

class User1(object):
 	name="QinAi" #public Attribute
 	__password="123456"
 	def __init__(self,sex,username):
 		self.sex=sex
 		self.username=username

u=User1("man","wanghuineng")
print(u.name)
print(u.username)

class A(object):
	name="wanghuineng"
	def test1(self):
		print("++"*30)
	@classmethod
	def test2(cls):
		cls.name="Aiqing"

		print("==="*30)
	@staticmethod 
	def test3():
		bane="buzhidao"
		print(bane)
		
a=A()
a.test2()  
a.test1()
print(A.name)
a.test3()


class Wang(object):
	def __init__(self,username,password):
		self.username=username
		self.password=password
		print("对象已经构造好了，由解释器自动调用的方法")

	def __new__(cls,username,password):
		print("类的对象开始创建")

u=Wang("buzhidao","xiaobai")
print(u)#这里是因为它没有返回当前类的对象，NEW方法里面没有返回，那么执行完第9行就自动终止,对象并没有被真正创建


class Wang1(object):
	def __init__(self,username,password):
		self.username=username
		self.password=password
		print("对象已经构造好了，由解释器自动调用的方法")

	def __new__(cls,username,password):

		print("类的对象开始创建")
		return object.__new__(cls)
	def __str__(self):
		return "用户名为%s，密码为%s"%(self.username,self.password)
u1=Wang1("buzhidao","wotaibeng")
print(u1)

class Wang2(object):
	def __init__(self,name):
		self.name=name
w1=Wang2("wanghuineng")
w2=Wang2("wanghuineng")
print(w1==w2)
print(id(w1),id(w2))

#单例模式1
class Wang3(object):
	__instance=None
	def __init__(self,name):
		self.name=name
	@classmethod
	def get_instance(cls,name):
		if not cls.__instance:
			cls.__instance=Wang3(name)
		return cls.__instance
w3=Wang3.get_instance("wanghuineng")
w4=Wang3.get_instance("buzhidao")
print(w3==w4)
print(id(w3),id(w4))
print(w3)
#这里只调用了get这个方法

#单例模式2
class Wang4(object):
	__instance=None
	def __init__(self,name):
		self.name=name
	def __new__(cls,name):
		if not cls.__instance:
			cls.__instance=object.__new__(cls)
		return cls.__instance
w5=Wang4("wanghuineng")
w6=Wang4("roubao")
print(w5==w6)
print(w5.name)
print(w6.name)
#NEW 方法结束之后，还会继续调用init方法

#设计模式 工厂模式 提高系统的维护性和拓展性
#解决代码的强依赖性的问题
#简单工厂类
class Person(object):
	def __init__(self,name):
		self.name=name
	def work(self,axe_type):

		print(self.name+"start to work")
		axe=Factory.creat_axe(axe_type)
		axe.cut_tree()
class Axe(object):
	def __init__(self,name):
		self.name=name
	def cut_tree(self):
		print("%s  use the axe to start to cut tree"%self.name)
class StoneAxe(Axe):
	def cut_tree(self):
		print("use the StoneAxe to cut down the tree")
class SteelAxe(Axe):
	def cut_tree(self):
		print("use the SteelAxe to cut down the tree")
class Factory(object):
	@staticmethod
	def creat_axe(type):
		if type=="stone":
			return StoneAxe("StoneAxe")
		elif type=="steel":
			return SteelAxe("SteelAxe")
		else:
			print("the choice is not existed")
p=Person("wanghuineng")
p.work("stone")


#工厂模式 就不是简单的选择，而是说同时有很多个工厂
class Person(object):
	def __init__(self,name):
		self.name=name
	def work(self):

		print(self.name+"start to work")
		axe=Stone_Axe_Factory().creat_axe()
		axe.cut_tree()
class Axe(object):
	def __init__(self,name):
		self.name=name
	def cut_tree(self):
		print("%s  use the axe to start to cut tree"%self.name)
class StoneAxe(Axe):
	def cut_tree(self):
		print("use the StoneAxe to cut down the tree")
class SteelAxe(Axe):
	def cut_tree(self):
		print("use the SteelAxe to cut down the tree")
class Factory(object):
	def creat_axe(self):
		pass
class Stone_Axe_Factory(Factory):
	def creat_axe(self):
		return StoneAxe("StoneAxe")
class Steel_Axe_Factory(Factory):
	def creat_axe(self):
		return SteelAxe("SteelAxe")
p=Person("wanghuineng")
p.work()
 

