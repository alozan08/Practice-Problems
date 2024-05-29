def print_menu():
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')


def get_num_of_non_WS_character(sample_txt):
    count = 0
    for i in sample_txt:
        if not i.isspace():
            count += 1
    return count

def get_num_of_words(sample_txt):
    count = len(sample_txt.split())
    return count

def fix_capitalization(sample_txt):
    corrected = ''
    firstLetter = True
    count = 0
    for c in sample_txt:
        if c.isalpha() and firstLetter == True:
            if c.islower():
                corrected += c.upper()
                count += 1
                firstLetter = False
            else:
                corrected += c
                firstLetter = False
        elif c == '.':
            corrected += c
            firstLetter = True
        else:
            corrected += c

    return corrected, count


def replace_punctuation(sample_txt, exclamation_count = 0, semicolon_count = 0):
    corrected = ''
    for c in sample_txt:
        if c == '!':
            corrected += '.'
            exclamation_count += 1
        elif c == ';':
            corrected += ','
            semicolon_count += 1
        else:
            corrected += c
    return corrected, exclamation_count, semicolon_count


def shorten_space(sample_text):
    sample_txt = sample_text.replace('  ', ' ')
    return sample_txt


def execute_menu(choice, sample_txt):
    if choice == 'c':
        non_ws = get_num_of_non_WS_character(sample_txt)
        print(f'Number of non-whitespace characters: {non_ws}')
    elif choice == 'w':
        word_count = get_num_of_words(sample_txt)
        print(f'Number of words: {word_count}')
    elif choice == 'f':
        fixed, count = fix_capitalization(sample_txt)
        print(f'Number of letters capitalized: {count}')
        print(f'Edited text: {fixed}')
    elif choice == 'r':
        fixed, exc_count, sem_count = replace_punctuation(sample_txt)
        print('Punctuation replaced')
        print(f'exclamation_count: {exc_count}')
        print(f'sem_count: {sem_count}')
        print(f'Edited_text: {fixed}')
    else:
        fixed = shorten_space(sample_txt)
        print(f'Edited text: {fixed}')


user_input = input('Enter a sample text:\n')
print('\nYou entered:', user_input)
print_menu()
options = ['c', 'w', 'f', 'r', 's', 'q']

choice = input('Choose an option:\n')

while choice != 'q':
    if choice not in options:
        choice = input('Choose an option:\n')
        continue
    execute_menu(choice, user_input)
    print_menu()
    choice = input('Choose an option:\n')



