#Example1: creating dictionary
""" mydic={101:'x',102:'y',103:'z'}
print(mydic) """

#Example2: access items from dictionary
""" mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2021'}
print(mydic['brand'])

#using get()
x=mydic.get('brand')
print(mydic.get('brand')) #hyudai """

#Example3: change value in dictionary
""" mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
}
print(mydic)
mydic['year']=2021 #new value
print(mydic) """

#Example4: reading items from dictionary using loop

""" mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
} """
""" for i in mydic:
    print(i) # prints only keys from dictionary

for i in mydic:
    print(mydic[i]) #print only values from dictionary

for i in mydic.values():
    print(i) """

""" for x,y in mydic.items():
    print(x,y) #print keys along with values """

#Example5: check key is exist in dictionary or not
# mydic={
#     'brand': 'hyudai',
#     'model': 'i10',
#     'year': '2020'
# }

""" if 'model' in mydic:
    print('exits') #true
else:
    print('not exist') """

# print('model' in mydic)

#Example6: find number of items in dictonary
""" mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
}

print(len(mydic))
 """
#Adding items to dictionary
""" mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
}

mydic['color']='red'
print(mydic) """

#Remove item from dictionary
mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
}
""" mydic.pop('year')
print(mydic) """

""" del mydic['year']
print(mydic) """

""" del mydic
print(mydic) #NameError: name 'mydic' is not defined
 """
""" mydic.clear() #clear all elements
print(mydic) #{} """

#Example9: copying dictionary
mydic={
    'brand': 'hyudai',
    'model': 'i10',
    'year': '2020'
}

#using copy()
mydic2=mydic.copy()
print(mydic2)


#without using copy()
""" mydic2=mydic
print(mydic2) #{'brand': 'hyudai', 'model': 'i10', 'year': '2020'}
 """
