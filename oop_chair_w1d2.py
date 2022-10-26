
from codecs import charmap_build


# chair


# class Chair:
#     pass


# x=Chair
# print(x)

###### lets make an instance of chair
class Chair:
    def __init__(self):
        self.color="red"
        self.size=3

# let's make an instance of chair
#x=Chair('black')
x=Chair()
print(x.color, x.size)
########
class Chair:
    def __init__(self,abc,numb,f): # init is class constructor
        self.color=abc   # color and size and price are class attributes
        self.size=numb
        self.price=f

    def chair_roles(self):  # chaire_roles is a method of Chair
       print( " I can role ")

    

# let's make an instance of chair
x=Chair('black',5,40)  # a class instance
print(x.color, x.size,x.price)

y=Chair   # a class

x.chair_roles()


########  class 

class Chair:
    number_of_chairs=0  # is a Class attribute not an instance attribute
    def __init__(self,abc,numb,f): # init is class constructor
        self.color=abc   # color and size and price are class attributes
        self.size=numb
        self.price=f
        Chair.number_of_chairs+=1

    def chair_roles(self):  # chaire_roles is a method of Chair
       print( " I can role ")

    def sell_the_chair(self,sell_price=100):
        print(f" We sold the {self.color} chair for {sell_price}")

        profit=sell_price-self.
        Chair.number_of_chairs-=1
        return profit

    

x1=Chair("Red",4,60)
x2=Chair("Black",3,40)
x3=Chair("yellow",5,70)

print(Chair.number_of_chairs)
print(x1.number_of_chairs)

x1.color='Orange'
print(x1.color)

x1.size=2*x1.size
print(x1.size)
print(Chair.number_of_chairs)

print(x1.sell_the_chair())
print(Chair.number_of_chairs)

print(x1.sell_the_chair(150))
print(Chair.number_of_chairs)






