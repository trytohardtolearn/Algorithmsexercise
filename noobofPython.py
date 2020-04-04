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
		self.name="xiaobai"
	def eat(self):
		print("eat something")
	def sleep(self):
		print("sleep")

class Dog(Animal):
	def __init__(self,name):
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
za.eat()
 