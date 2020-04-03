class User1:
	def __init__(self,password):
		if len(password)>=6:
			self._password=password
		else:
			print("you have inputed the wrong length of password")

	def __str__(self):
		return "the password is %s"%self._password
u2=User1("123")
print(u2)
