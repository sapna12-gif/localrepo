#Example1:byfeault we create argument 'self'

""" class MyClass:
    def myfunc(self):
        pass
    def display(self):
        print('sapna')

mc1=MyClass() #Object
mc2=MyClass()
mc1.display() #access method """

#Example2:
class MyClass:
    def m1(self):
        print('this is instance method...')
    
    @staticmethod
    def m2(self,num):
        print(self,num)
mc=MyClass()
mc.m1()
mc.m2(100,200)

#MyClass.m2(10,20) #10,20 #here calling static method directly using class not through object.

#Example3:

class MyClass:
    a,b=10,20 # class variables
    def add(self):
        print(self.a+self.b)
    def nul(self):
        print(self.a+self.b)
mc=MyClass()
mc.add()
mc.nul()
