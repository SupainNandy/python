#Inheritence
from enum import member
class User:
    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("enroll")

    def review(self):
        print("Review")



s1=User()

# s1.login()

#Example 2
#Constuctor Inherritance-> if the child class not have any constuctor so that parent constuctor call 
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")

        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("buying phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying Samart Phone")
        super().buy()

p1=SmartPhone(2000,"Samsung",100)
print(p1.brand)



#Example 3
# Inheriting Private member -> child class cant access the parent call hiding object


# Example-> Method Overridinge -> parent class method name and child class method name same but difrent task
# p1.buy()


#Example 4:
#Super Key ->Super() keyword is used to call the parent class constructor or method
#super key cant work outside the class

p1.buy()

