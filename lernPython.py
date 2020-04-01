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
