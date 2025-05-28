# Example1: how to create List

""" mylist1 = [10,20,30,40,50,60,70]
mylist2 = ['apple','banana','cherry']
mylist3 = ['apple',10,'banana',20]
mylist = list()

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist) """

# Example2: Accessing items from the list
""" mylist=['apple','banana','cherry'] # idex starts from 0

print(mylist[0])
print(mylist[-1]) # -1 means last one. """

# Example3: Range of Indexes
""" mylist=['apple','banana','cherry','orange','melon','mango']
print(mylist[2:5])
print(mylist[-4:-1]) """

#Example4: Change item value
""" mylist = ['apple','banana','cherry']
print(mylist) #['apple','banana','cherry']
mylist[0] ='orange' # this will chnge the value based on index
print(mylist) #['orange','banana','cherry'] """

#Example5: read the items using loop statement
""" mylist = ['apple','banana','cherry']

for i in mylist:
    print(i) """

# Example6: check if the item is exist in the lis or not
""" mylist = ['apple','banana','cherry']

if 'apple' in mylist:
    print('yes, apple is present')
else:
    print('No, apple is not present') """

#Example7: List Length(counting number of items in list)
""" mylist = ['apple','banana', 'cherry']
print(len(mylist)) #3 """

#Example8: Add items append() insert()
""" mylist = ['apple','banana','cherry']
mylist.append('orange') #append add new item at end of list
print(mylist)  # ['apple', 'banana', 'cherry', 'orange']"""


""" mylist = ['apple','banana','cherry']
mylist.insert(1,'orange') #insert add new item anywhere of list
print(mylist) """

#Example9: Remove item from the list
#pop()
""" mylist = ['apple','banana','cherry']
mylist.pop(0) # here we should specify index not value
print(mylist) """

#del is keyword
""" mylist = ['apple','banana','cherry']
del mylist[2] # here del command removes single item based on the index
print(mylist) """

#clear()
mylist = ['apple','banana','cherry']
mylist.clear()
print(mylist)

# Example10: copy list 
#list()
""" mylist=['apple', 'banana', 'cherry', 'orange']
mylist2=list(mylist)
print(mylist) #['apple', 'banana', 'cherry', 'orange']
print(mylist2) #['apple', 'banana', 'cherry', 'orange'] """

#copy()
""" mylist=['apple', 'banana', 'cherry', 'orange']
mylist2=mylist.copy()
print(mylist) #['apple', 'banana', 'cherry', 'orange']
print(mylist2) """

#Example11: Combine/join lists
#using + operator
""" list1 = ['a','b','c','d']
list2 = [1, 2, 3, 4]
List3 = list1+list2
print(List3) """

# using loop statement
""" list1 = ['a','b','c','d']
list2 = [1, 2, 3, 4]

for i in list2:
    list1.append(i)
print(list1) """

#using extend()
""" list1 = ['a','b','c','d']
list2 = [1, 2, 3, 4]
list1.extend(list2)
print(list1) """

#List comparison
list1 = (10,20,30)
list2 = ('a','b','c','d')

if list1==list2:
    print('list are equal')
else:
    print('list are not equal')


