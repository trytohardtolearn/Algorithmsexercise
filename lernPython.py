class Car:
	def start(self):
		print("hello world")
	def print_car_inf(self):
	    print("Output the car's attribute:%s,%s"%(self.name,self.color))	
c=Car()#creat a Objection
c2=Car()#creat other Obejection
#c.start()
c.name="Benz"
c.color="black"
c.print_car_inf()





class Person:
	def __init__(self):
		self.name="Wanghuineng"
		self.age="26"
		self.height="172"
	def work(self):
		pass
pl=Person()
print(pl.name)


class Person1:
	def __init__(self,name,age,height):
		self.name=name
		self.age=age
		self.height=height
	def __str__(self):
		return "Name=%s,Age=%s"%(self.name,self.age)
	def introduce(self):
		print("Name=%s,Age=%s"%(self.name,self.age))
pl1=Person1("Wanghuineng",26,171)
print(pl1)




# the Gambel Game
import random
class Game:
	def __init__(self,player1,player2):
		self.player1=player1
		self.player2=player2
		print("the Game is successfully initiated")
	def start(self):
	    self.player1.ThrowDice()
	    self.player2.ThrowDice()
	    print(self.player1)
	    print(self.player2)

class Player:
    def __init__(self,name,sex,*dice):
        self.name=name
        self.sex=sex
        self.dices=dice #here is a tuple
    def ThrowDice(self):
    	for dice in self.dices:
    		dice.Move()
    def Say_Dice(self,number1,number2):
    	return (4,2)
    def __str__(self):
    	player_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
    	return "PlayersName=%s,PlayersNumber=%s"%(self.name,str(player_dice_count_list))
class Dice:
	def __init__(self):
		self.count=0
	def Move(self):
		self.count=random.randint(1,6)
    	


#before starting game we are prepared six dices
d1=Dice()
d2=Dice()
d3=Dice()
d4=Dice()
d5=Dice()
d6=Dice()

p1=Player("wang","man",d1,d2,d3)
p2=Player("Bao","women",d4,d5,d6)

for i in range(1,6):
	print("the Number of the times : %s"%i)
	game=Game(p1,p2)
	game.start()
	sum1=d1.count+d2.count+d3.count
	sum2=d4.count+d5.count+d6.count
	if sum1<sum2:
		print("Bao wins")
	elif sum1==sum2:
		print("nobody wins")
	else:
		print("wang wins")



class User:

	def __init__(self,passwort_length):
		if len(passwort_length)>=6:
			self.passwort=passwort_length
		else:
			print("you have inputed the wrong length of passwort")
	def __str__(self):
		return " passwort=%s "%self.passwort
	def get_password(self):
		return self.passwort

u1=User("1231231231")
print(u1.get_password())


class User2:
	def __init__(self):
		print("the object will be created")
	def __del__(self):
		print("the object will be deleted")

u1=User2()
u2=u1
del u1
print("=="*30)
del u2
print("``"*30)


class Animal:
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
m1=Dog()
m1.eat()


class A:
	def Test(self):
		print("A----test()")
class B:
	def Test(self):
		print("B---test()")
class C1(A,B):
	def test1(self):
		print("C---test()")
class C2(B,A):
	def test2(self):
		print("C2--test()")
c=C2()
c.Test()
m=C1()
m.Test()


#How to deal with the Error
try:
	print(a)
	i=1/0
except (NameError,ZeroDivisionError) as ex:#ex 代表你刚刚捕获的异常
	print("Exist a Error")#捕获完一种异常之后不会回头再继续执行之前的代码
	print(ex)
print("world") # 捕获异常之后，程序可以继续往下面跑


a="123"
f=open("text.txt","w")
try:
    f.write("hello\n")
    f.write("world %d"%a)
except Exception as ex:
	print(ex)
finally:#不管前面代码有没有出错，最终要执行的代码
	f.close()

	