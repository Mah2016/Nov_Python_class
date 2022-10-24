

print("hello")
x=2
y=x*3
print(x,y)
my_float_variable=3.56
print(my_float_variable)


my_string="this is a string"
print(my_string)

# this makes a comment that means it won't be run.

# this one is a boolian variable
x=True

print("this is an example to show the indices")

print("this is an example to show the indices"[2])

y="this is an example to show the indices"
print(y[3:10])

a= " red"
b=" apple"
print(" this is the result of a plus b:", a+b, " this is the continuation")
# example of f-string:
print(f" this is the result of a plus b: {a+b} this is the continuation")


print(f" another example {x} , how it works??")

# some built-in functions for strings

x="a lower case string"
print(x.upper())
#print(dir(x))

print(len(x))
print(x.find("s"))

my_list=[2,None, "a string", [1,2]]
print(my_list)
print(my_list[2:])
print(my_list[2][5])

my_list[1]=True

print(my_list)

print(len(my_list))
my_list.append(8)
print(my_list.pop())
print(my_list)
x=[13,2,6,8]
y=x.sort()
print(y)
print(x)
z=sorted(x)
print(x)
print(z)

my_car={"name":"my 1st car", "brand":"Honda" , "price":5000}
print(type(my_car))
print(my_car["price"])

my_list=[2,None, "a string", [1,2], my_car]

print(my_list)

print(my_list[4]['brand'])



### afternoon session



x=[3,6,2]
y=(4,6,2) # tuple  immutable

print(x)
print(y)
z=list(y)
print(z,f"z is a {type(z)}")

### function ######
# in js:
# function name(){

# }

# in python:
def name_of_function(input_str):
    ...
    return result


x=2
y=3

def add_two_numbers (a, b):  # a and b are parameters of the function
    return a+b

print(add_two_numbers(4,5)) # 4 and 5 are arguments for the function 

z= add_two_numbers(8+9,5)
print(z)


my_car={"name":"my 1st car", "brand":"Honda" , "price":5000}

def manupulate_dictionary(d):

    return d["name"]+" it 's not correct"

print(manupulate_dictionary(my_car))

another_input=[1,3]
#print(manupulate_dictionary(another_input))


def an_example(my_number,my_str):

    a= my_number * my_str
    return a

print(an_example(3," Coding Dojo"))


######## loops: ######

# in js:
# for ( var i=1; i<10, i++){
# ...
# }

for i in [1,2,3]:

    print(i)

for i in "abxy":
    print(i)

for i in range(3,8,2):
    print(i)

for i in range(3,18,2):
    if i==10:
        break
    print(i)

for i in range(3,18,1):
    if i==11:
        continue  # don't do anything and return to the loop for next i
    print(i)


my_str=" this is an example"
result=""
for i in my_str:
    result = i+result

print(result)

result=""
i=0
while my_str[i] is not "s":
    i=i+1
    result += my_str[i]

print(result) 

x=[2,4,6,7,8,1]
i=3
while x[i]<5:
    i+=1
    print(i,x[i])


for i in range(len(x)):
    if x[i]<5:
        print(i, x[i])


x=[3,4,5]
print(x)
x[1]=10
print(x)

x=(3,4,5)
print(x)
# x[1]=10
# print(x)
y=list(x)

y[2]=10
print("this is y",y)

del x
print(x)






































