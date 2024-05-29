'''
    Write a program to draw a right-justified triangle given the height as input
    the first row has one * and increases by one for each row.
    Each asterisk is followed by a blank space and each row ends with a new line
'''

x = int(input("Enter the height: "))

for i in range(1, x + 1):
    for j in range(x - i):
        print(' ', end = ' ')
    for k in range(i):
        print('*', end = ' ')
    print()

# UPSIDE DOWN TRIANGLE

x = int(input("Enter a number: "))

for i in range(x , 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()