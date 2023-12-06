from random import*
class Student: 
    def init(self, height=160):
         self.height = height
    def grow(self, height):
         self.height+=height
    def fall(self, height):
         self.height-=height
a = " year later"
ni = "nick: "
ka = "kate: "
nick = Student()
kate = Student(height=170)
nick.grow(height=randint(1, 20))
kate.fall(height=randint(1, 20))
print(ni, nick.height)
print(ka, kate.height)
print(randint(1, 5), a)
nick.fall(height=randint(1, 20))
kate.grow(height=randint(1, 20))
print(ni, nick.height)
print(ka, kate.height)
print(randint(1, 5), a)
nick.grow(height=randint(1, 20))
kate.fall(height=randint(1, 20))
print(ni, nick.height)
print(ka, kate.height)
print(randint(1, 5), a)
nick.fall(height=randint(1, 20))
kate.grow(height=randint(1, 20))
print(ni, nick.height)
print(ka, kate.height)