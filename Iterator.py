# mytuple = ('name', 'age', 'speed')
# mystr = 'saySomethin'
# myit = iter(mystr)

# print(myit)
# for i in myit:
#     print(i)

# class MyNumbers:
#     def __init__(self, name : str, age : int) -> None:
#         self.name = name
#         self.age = age

#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myClass = MyNumbers('J', 20)

# myIter = iter(myClass)

# for i in myIter:
#     print(i)

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    Vehicle.move(self)
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()