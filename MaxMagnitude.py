'''
    Write a function max_magnitude with 3 int parameters that returns the largest magnitude value
    use the function in the main program that takes 3 integer inputs and outputs the largest magnitude value

'''
import math


def max_magnitude(num1, num2, num3):
    abs1 = abs(num1)
    abs2 = abs(num2)
    abs3 = abs(num3)
    largest = max(abs1, abs2, abs3)
    if largest == abs1:
        return num1
    elif largest == abs2:
        return num2
    else:
        return num3

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(max_magnitude(num1, num2, num3))
