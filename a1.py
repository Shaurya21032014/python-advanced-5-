# Parent class
class dad:

    def __init__(self, eyes , aggresive):
        self.eyes = eyes 
        self.aggressive = aggressive

    def display(self):
        print("your eyes color is ", self.eyes)
        print("you are aggressive ", self.aggressive)


# Child class 
class son(dad):
    def __init__(self , name , age , eyes , aggressive):
        self.name = name
        self.age = age

    def __init__(self, name, age, eyes, aggressive):
        self.name = name 
        self.age = age

    # inoking the  __init__ of parent class 
    # to access its attributes
        dad.__init__(self, eyes, aggressive)

# Object Creation 
obj = son("penguin" , 8, "blue" , True)




# Calling method display 
obj.display


