from types import coroutine
from os import cpu_count
class Coustomer:
     def __init__(self,name,gender):
        self.name =  name
        self.gender = gender

     def __str__(self):
        return f"Customer(name=`{self.name},gender=`{self.gender}`)"

#pass by refferenc
def greet(costomer):
    if costomer.gender =="male":
        print("Hello",costomer.name,"sir")
    else:
        print("Hello",costomer.name,"maam")


cust = Coustomer("Rimi","female")


greet(cust)