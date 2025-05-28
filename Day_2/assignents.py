# 1. Check the given number is postive or negative
""" num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") """

#2. Check the largest of two number

""" num1 = float(input("Enter first number: "))  # Get two numbers from the user
num2 = float(input("Enter second number: "))

if num1 > num2:  # Compare the numbers
    print("The first number is larger.")
elif num2 > num1:
    print("The second number is larger.")
else:
    print("Both numbers are equal.") """

# Check the largest of three number
""" num1= float(input("Enter a first number:"))
num2= float(input("Enter a second number:"))
num3= float(input("Enter a third number:"))

if num1 >= num2 and num1 >= num3:
    print("The first number is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("The second number is the largest.")
else:
    print("The third number is the largest.") """

# print week number if you provide weekname as input
weekname = input("Enter week name: ").strip().lower()

if weekname == "monday":
    print(1)
elif weekname == "tuesday":
    print(2)
elif weekname == "wednesday":
    print(3)
elif weekname == "thursday":
    print(4)
elif weekname == "friday":
    print(5)
elif weekname == "saturday":
    print(6)
elif weekname == "sunday":
    print(7)
else:
    print("Invalid week name")


