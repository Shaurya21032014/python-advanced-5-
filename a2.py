# import necessary packages 
from abc import ABC , abstractclassmethod
# create a base class 
class Animal (ABC):
    




    # abstract method 
         # should be implemented by all sub-classes
         def move (self):
                 pass
           

# sub class 
class human(Animal):
        

        def move(self):
                print("i can walk and run")


class Snake(Animal):
          def move(self):
                  print("i can crawl")

class Dog(Animal):
          def move(self):
                  print("i can barkk")


class lion(Animal):
          def move(self):
                  print("i can roar")

# driver code 
r = human()
r.move()

k = Snake()
k.move()

r = Dog
r.move()


k = lion()
k.move()
  
