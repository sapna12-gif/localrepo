# Example1:

""" def func(i,j):
    print(i,j)

# func(10,20) #positional arguments
func(j=20,i=10) #keyword arguments """

#Example2:default values assigned to positional arguments
""" def func(i,j=10):
    print(i,j)

func(100,200) #100 200
func(100) #100, 10 """

#Example3: keyword arguments
""" def greetings(name,greetmsg):
    print(greetmsg+' '+name)

greetings(name='Jhon',greetmsg="Hello")#Hello Jhon
greetings(greetmsg="hello",name = 'John') """

#Example4:
""" def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30) #postional paramteres
my_func(a=10,b=20,c=30) #keyword arguments
my_func(b=20,a=10,c=30) #keyword argument, we can change the order also

my_func(10,20,c=30) #cmobination of postional and keyword
 """
#my_func(10,b=20,30) # this is wrong as postional argument must appear before any keyword argument
#my_func(10,30, b=20) this is having local error

#Example5: 
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a

""" print(largest(100, 200))
print(largest(20,10)) #(20,10), return mutilple value 
"""

res = largest(10,20)
print(res)
