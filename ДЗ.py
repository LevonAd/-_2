class Dog:
 amount_of_dogs = 0
 def __init__(self, size=160):
    self.size = size
    Dog.amount_of_dogs += 1
 
nick_dog = Dog()
kate_dog = Dog(size=170)
nick_cat = Dog(size=130)
anton_cat = Dog(size=300)
print(nick_dog.size)
print(kate_dog.size)
print(nick_cat.size)
print(anton_cat.size)
print(nick_dog.amount_of_dogs)