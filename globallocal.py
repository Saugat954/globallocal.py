

#Gloval and lical variable in pyhton
x = 4 #global variable
print(f"The global variable X is {x}")

def hello():
    x=5 #local variable
    print(f"The local variable X is {x}")

hello()

#To make change in global variable inside function we can use global keyword
y = 4 #global variable
print(f"The global variable Y is {y}")

def hello():
    global y
    y=5 #local variable
    print(f"The local variable X is {y}")

hello()
print(f"The global variable has changed into {y}")