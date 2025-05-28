#Example1: Creating tuple
""" mytuple =('apple','banana','orange')
print(mytuple) """

#Example2: access tuple itmes
""" mytuple =('apple','banana','orange')
print(mytuple[1]) """

#Example3: range of idexes
""" mytuple=('apple','banana','cherry','orange','abc')
print(mytuple[2:5]) #('cherry', 'orange')
print(mytuple[-4:-1]) #('apple', 'banana', 'cherry') """

#Example 4: Changing tuple items/value
# by default tuple does not allow you change value becoz it is immutable 
# but there is work around
# tuple--->List(modity)--->tuple
""" mytuple =('apple','banana','cherry')
mylist=list(mytuple)
mylist[0]='orange'
mytuple=tuple(mylist)
print(mytuple)
 """

#Example5: Reading tuple items using loop
""" mytuple=('apple','banana','cherry')
for i in mytuple:
    print(i) """

#Example6: Check if Item Exists(searching of item in tuple)
""" mytuple=('apple','banana','cherry')

if 'banana' in mytuple:
    print('yes, banana is present')
else:
    print('no, banana is not present') """

#Example7: Tuple Length - counting itmes in a tuple
""" mytuple=('apple','banana','cherry')
print(len(mytuple)) #3 """

#Example8: Add itmes to tuple- not possible bcoz tuple is immutable - cannot change values/items
""" mytuple=('apple','banana','cherry')
mytuple[0] = 'orange' #TypeError: 'tuple' object does not support item assignment
print(mytuple) """

#Example9: copy tuple 
""" mytuple=('apple','banana','cherry')
mytuple2=mytuple
print(mytuple2) """

#Example10: removing items from tuple - not possible becoz tuple is immutable
mytuple=('apple','banana','cherry')
# mytuple.remove('apple') #invalid / it is not possible
#del mytuple
#print(mytuple) #NameError: name 'mytuple' is not defined

#Example11: Join/combine tuple
""" tuple1 = (10,20,30)
tuple2 = ('a','b','c','d')

tuple3 = tuple1+tuple2
print(tuple3) """

#Example12:
tuple1 = (10,20,30)
tuple2 = ('a','b','c','d')

if tuple1==tuple2:
    print('tuples are equal')
else:
    print('tuples are not equal')
