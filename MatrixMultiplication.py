'''
    A matrix is a rectangel of numbers in rows and colums.
    1xN matrix: one row, N columns
    NxN matrix: N rows, N columns
    Multiplying a 1xN matrix (A) by a NxN matrix (B) produces a 1xN matrix (C)
    To determine the Nth element of C, multiply each element of A by each element of the Nth column of B
    Write a program that reads a 1xN matrix (A) and a NxN matrix (B), and outputs the
    1xN matrix product, C.
    N can be of any size >= 2
    A is represented as a list of the integers found on the first line of input
    B is represented as a list of N rows, each of which is a list of N integers.
    Each of the next N input lines contains the integers for one row of B
        Note: input is one row at a time but multiplication uses columns of B
    For coding simplicity, follow each output integer by a space, even the last one. Output ends with a newline
'''

matrixA =  [int(n) for n in input().split()]
n = len(matrixA)

# _ is used as a dummy variable in the outer loop. Common approach when the value of the loop variable isn't needed
# in the loop body. Any value can be used (i.e. 'i'), won't affect the logic/output
matrixB = [[int(n) for n in input().split()] for _ in range(n)]

matrixC = [0] * n


for i in range(n):
    for j in range(n):
        matrixC[i] += matrixA[j] * matrixB[j][i]

for val in matrixC:
    print(val, end = ' ')