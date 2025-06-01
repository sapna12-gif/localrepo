#write a program or pseudocode that print  the number 1 to 10. but for multiples of three print' 'Fizz' instead of number and for multiples of five print 'Buzz' for  number which are multiples of both three and five 'FizzBuzz'.
for i in range(1,11):
    if i % 3 == 0 and i % 5 ==0:
        print('FizzBuzz')
    elif i % 3==0:
        print('Fizz')
    elif i % 5==0:
        print("Bizz")
    else:
        print(i)