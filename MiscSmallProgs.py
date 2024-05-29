#   Write a program that reads a list of words. Then, the program outputs those words and their
#   frequencies (case-insensitive)

words = [s for s in input().split()]
u_words = [s.upper() for s in words]

for i in range(len(u_words)):
    count = u_words.count(u_words[i])
    print(f'{words[i]} {count}')


#######################################################################################################################
#   Scrabble is a word game in which words are constructed from letter tiels, each letter containing a point value
#   The value of a word is the sum of each title's points added to any points provided by the word's placement on
#   the board.
#   Write a program using the given dictionary of letters and point values that takes a word as input and outputs
#   the base total value of the word (before being put onto a board)

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }


word = input()
points = 0

for letter in word:
    points += tile_dict[letter]

print(points)


#######################################################################################################################
# Complete the reverse_list() function that returns a new string list containing all contents in the param but in reverse
# DO NOT USE REVERSE() OR REVERSED()

def reverse_list(letters):
    reversed = []
    for i in range(len(letters) - 1, -1, -1):
        reversed.append(letters[i])
    return reversed


if __name__ == '__main__':
    ch = ['a', 'b', 'c']
    print(reverse_list(ch))  # Should print ['c', 'b', 'a']


#######################################################################################################################
# People's weights - lists

weights = []
for i in range(1,5):
    weight = w1 = float(input(f'Enter weight {i}:'))
    weights.append(weight)

average = sum(weights)/len(weights)
max_weight = max(weights)

print(f'Average weight: {average:.2f}')
print(f'Max weight: {max_weight:.2f}')
print()

loc = int(input("Enter a list location (1-4):\n")) - 1
kg = weights[loc] / 2.2
print(f'Weight in pounds: {weights[loc]:.2f}')
print(f'Weight in kilograms: {kg:.2f}')

sorted_w = sorted(weights)
print(f'Sorted weights: {sorted_w}')


#######################################################################################################################
# Write a program that reads a list of int from input and determines if the lists is a palindrome. The input
# begins with an integer indicating the length of the list that follows. Assume that the list will always contain
# fewer thaan 20 ins. Output 'yes' if the list is a palindrome and 'no' otherwise. Output ends with newline

list_len = int(input("Enter the length of list: "))
nums = []

for i in range(0,list_len):
    nums.append(int(input("Enter the number: ")))

if nums == nums[::-1]:
    print("yes")
else:
    print("no")


#######################################################################################################################
 # Write a prog that reads a list of integers from input and modifies the list by shifting each element
 # to the right one position and by shifting the last element to the first position.
 # Input begins with an int indicating the num of values that follow. output modified list, end w newline

list_size = int(input())
nums = []

for i in range(0, list_size):
    nums.append(int(input()))

last = nums.pop()
nums.insert(0, last)

for n in nums:
    print(n, end=' ')
print()


#######################################################################################################################
# Input is a sequence of ints that ends with -1. all other integers in the sequence are between 1 and 20 (inclusive)
# Total num of ints in the sequence is unknown. Output the mode and end with newline
# Assume sequence isn't empty and only one mode exists.
# Use a list to count the number of ocurrences of 1-20.
# num_count [] counts the number of occurrences for values 1-20 in the corresponding array index.
# Items in index 0 are ignored

num_count = [0] * 21  # Initialize a list of 21 0's for tallies
nums = []

num = int(input("Enter a number: "))
while num != -1:
    nums.append(num)
    num = int(input("Enter a number: "))

for num in nums:
    num_count[num] += 1

print(num_count.index(max(num_count)))


#######################################################################################################################
# write a program that reads a list of positive integers followed by a negative integer
# from input and outputs the Nth number from the end of the list.
# Convert the negative integer read at the end to positive and use as N.
# Output the negative integer read at the end if the size of the list is smaller than N.

nums = [int(n) for n in input().split()]
nth = int(input())

if nth * -1 <= len(nums):
    print(nums[nth])
else: print(nth)


#######################################################################################################################
# Write a program that reads two lists of integers and outputs the sum of multiplying the corresponding
# list items.
# Note: the size of the two lists must be the same.

n1 = [int(n) for n in input().split()]
n2 = [int(n) for n in input().split()]

if len(n1) == len(n2):
    result = 0

    for i in range(0, len(n1)):
        result += n1[i] * n2[i]
    print(result)


#######################################################################################################################
# Write a program that reads a list of integers from input and outputs 'yes' if the list is sorted in
# ascending order between the two provided positions.
# Otherwise, output 'no'. The first set of inputs is the list. The next two inputs are the start and end positions
# (inclusive)
# Assume position 1 is the first element of the list.

nums = [int(n) for n in input().split()]
start, end = [int(n) for n in input().split()]
start -= 1

nums_sort = sorted(nums[start:end])

if nums[start:end] == nums_sort:
    print('yes')
else:
    print('no')


#######################################################################################################################
class Number:
    def __init__(self, n):
        self.num = n

    def get_num(self):
        return self.num

    def set_num(self, n):
        self.num = n

def swap(num1, num2):
    temp = num1.get_num()
    num1.set_num(num2.get_num())
    num2.set_num(temp)


if __name__ == '__main__':
    int1 = int(input())
    int2 = int(input())

    num1 = Number(int1)
    num2 = Number(int2)

    swap(num1, num2)
    print('num1 =', num1.get_num(), 'and num2 =', num2.get_num())
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

