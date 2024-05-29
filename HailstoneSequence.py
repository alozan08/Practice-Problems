'''
    Given a positive integer n, the following rules will always create a sequence that ends with 1 (hailstone):
        if n is even, divide it by 2.
        if n is odd, multiply it by 3 and add 1 (3n+1)
        continue until n is 1
    Write a program that reads an integer as input and prints the hailstone sequence starting with the integer
    entered. Format the output so that ten integers, each separated be a tab are printed per line.
'''
num = int(input("Enter a positive integer n: "))
nums = []

counter = 0

while True:
    nums.append(num)
    if num == 1:
        break
    else:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1


for num in nums:
    print(int(num), end="\t")
    counter += 1
    if counter == 10:
        print()
        counter = 0