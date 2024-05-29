'''
    Write a program that reads two phrases on separate lines and outputs one of four responses:
        1) Phrase one is found within phrase two
        2) Phrase two is found within phrase one
        3) Both phrases match
        4) No matches

        Hint: Use membership operator in.
'''
word1 = input("Enter phrase one: ")
word2 = input("Enter phrase two: ")

if word1 == word2:
    print('Both phrases match')
elif word1 in word2:
    print(f'{word1} is found within {word2}')
elif word2 in word1:
    print(f'{word2} is found within {word1}')
else:
    print('No matches')