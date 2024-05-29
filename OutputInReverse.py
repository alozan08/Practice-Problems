'''
    Wrote a program that reads a list of integers, one per line, until a * is read
    then output those integers in reverse. For simplicity in coding outout, follow each integer, including the last one
    by a comma.
    use a while looop to output the integers. DO NOT use reverse() or reversed()
'''
nums = []
while True:
    num = input('Enter a number: ')
    if num ==  '*':
        break
    else:
        nums.append(int(num))

print(nums)
i = len(nums) - 1

while i >= 0:
    print(nums[i], end = ',')
    i -= 1
print()