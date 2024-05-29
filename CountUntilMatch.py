'''
    Write a program that takes in an integer in the range 11-100 as input.
    The output is a countdown starting from the integer, and stopping when both output digits are identical.
'''

num =  int(input("Enter a number: "))

if num not in range(11,101):
    print('invalid input')
else:
    while True:
        if num % 11 == 0:
            print(num)
            break
        else:
            print(num)
            num -= 1


