'''
    Write a program that outputs a downward facing arrow composed of a rectangle and a right triangle
    Arrow dimensions are defined by user specified arrow base height, arrow base width, and arrow had width
    1) Input the arrow base height and width. Draw a rectangle using *.
    2) Input the arrow head width and draw a right triangle
    3) Modify the program to only accept an arrow head width that's larger than the arrow base width. Use a loop
        to continue inputting the arrow head width until the value is larger than the arrow base width.
'''
height = int(input())
width = int(input())
arrow_head = 0

while arrow_head <= width:
    arrow_head = int(input())

for i in range(height):
    print('*' * width)

for i in range(arrow_head, 0, -1):
    print('*' * i)

