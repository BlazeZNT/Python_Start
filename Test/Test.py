
# snack = ["a","b","c"]

# for x in snack:
#     print (f"This is you snack number {x}")
    
    
# # val = 'Geeks'
# # print(f"{val}for{val} is a portal for {val}.")

# def add_num(a,b):
#     new_num = a+b
#     print(new_num)
    
# add_num(2,5)

file = open("Piano.txt","w")
file.write("Sinatra")
file.close()

from collections import Counter

my_counter = Counter("HELLO")

print(my_counter)
print(my_counter.most_common())

from datetime import date
from math import sqrt
from random import randint

my_date = date(1999,2,14)
# help(my_date)


class Triangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    @classmethod
    def random(cls):
        return cls(randint(1,20),randint(1,20))
    
    def get_hypotenuse(self):
        return sqrt(self.a **2 + self.b **2)
    
    def get_area(self):
        return self.a*self.b/2

        
t = Triangle(4,5)

print(t)
        
    
        
    
