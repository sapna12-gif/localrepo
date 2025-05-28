#Example1:
""" global_var =20 #global variable

def func():
    local_var=10 # local variable
    print(local_var)
    print(global_var)

func()

print(local_var) #invalid bcoz local_var is local variable of func()
print(global_var) """

#Example2: 
""" xy=100 #global variable

def cool():
    xy=200 #local variable
    print(xy) #this will print local variable.
cool() """

#Example3:Using Global variable in Local variable and upate value
""" xy=100 #global variable, change value of global inside the function

def cool():
    global xy
    xy=200 #global variable
    print(xy) #this will print local variable.
cool() #200 """

#Example4:
""" x=100

def cool():
    global x
    x=500
    print(x)
cool() #500
print(x) #500,invoke """

#Example5:we can also create inside the function but, we have to write global keyword
#There is no need to declare global variable outside the function .
# You can declare them global inside the function - global

def cool():
    global x #x is variable
    x=100
    print(x)
cool()
print(x) #able to access x boz it is global variable

