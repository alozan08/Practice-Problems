'''
    Write a program that first gets a list of integers from input.
    The input begins with an integer indicating the number of integers that follow.
    Then, get the last value from the input, which indicates a threshold.
    Output all integers less than or equal to that last threshold value.
'''

size = int(input())
nums = []

for i in range(size):
    nums.append(int(input()))

threshold = int(input())

for num in nums:
    if num <= threshold:
        print(num, end=',')