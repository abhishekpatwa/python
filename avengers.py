class Avengers:
	avengersCount = 0
	def __init__(self,name,power):
		Avengers.avengersCount += 1
		self.name=name
		self.power=power

	def howmany():
		print("total avengers %d" %Avengers.avengersCount)
		return Avengers.avengersCount

	def getname(self):
		print("avengers name:"+self.name+ "have power"+self.power)

hulk = Avengers("hulk","gussa")
print(hulk.name,hulk.power)
#abhishek  = Avengers("patwaji","never show our power")
print(hulk.name,hulk.power)
#notave= Avengers("")
print("avengersCount:", Avengers.avengersCount )
print("howmany",Avengers.howmany())
hulk.getname()

#python give a fcility to add atrribute afte the class like here i add hulk size
#we also overwrite name also and delete attribute also

#hulk.size= "very big"
#hulk.name= "very big"
#del (hulk.name)
#print(hulk.name) they nt work b/c del hulk.name

#getattr()   its use to get the any attribute like print(getattr(hulk,"name"))
#setattr()   its use to change attribute they exist setattr(hulk,"name","badahulk")
getattr(hulk,"name")
setattr(hulk,"name","lalhulk")
print(hulk.name)
