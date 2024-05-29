'''
    The midfix of 3 is the middle 3 characters of a string. Given a string input, output the middle
    3 characters of that string. Assume the word length is always odd and at least 3 characters.
'''

input_string = input("Enter input string:\n")

while input_string != 'q':
    if ',' in input_string:
        first, last = input_string.split(',')

        print(f'First word: {first.strip()}')
        print(f'Second word: {last.strip()}\n')
    else:
        print('Error: No comma in string.\n')


    input_string = input("Enter input string:\n")