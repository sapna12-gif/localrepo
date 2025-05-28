#Example1: Creating set
""" myset = {'apple','banana','cherry'}
print(myset) """

#Example2: Accessing items from set
""" myset = {'apple','banana','cherry'}
for i in myset:
    print(i) """

#Example3: value exits in set or not
""" myset = {'apple','banana','cherry'}

print('banana' in myset) #true
print('banana2' in myset) #False """

#Example: Adding items to set
#add()- add single item  update()-add multiple item
""" myset = {'apple','banana','cherry'}
# myset.add('orange')
myset.update(['mango','grapes'])
print(myset) # {'orange','apple','banana','cherry'}
            #{'grapes', 'apple', 'mango', """ 'banana', 'cherry'

#Example5: Find number of items in a set.
""" myset={'apple','banana','cherry'}
print(len(myset)) #3
 """

#Example6: remove item from set - remove() discard()
# myset = {'apple','banana','cherry'}
""" myset.remove('banana')
print(myset) """
#myset.discard('xyz') -- #keyError: 'xyz'

""" myset.discard('banana')
print(myset)
myset.discard('xyz') # will not throw any error """

#Example7: clear all items from set
""" myset = {'apple','banana','cherry'}
myset.clear()
print(myset) #set() """

""" myset = {'apple','banana','cherry'}
del myset
print(myset) #set() """


#Example8: joining 2 sets -union()
""" set1={'a','b','c','d'}
set2= {1,2,3}
set3=set1.union(set2)
print(set3) """

#upate()
set1={'a','b','c','d'}
set2= {1,2,3}
set1.update(set2)
print(set1)