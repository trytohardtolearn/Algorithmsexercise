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

