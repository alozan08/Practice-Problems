def print_table(t, h1, h2, strs, ints):
    print(f'{t:>33}')
    print(f'{h1:<20}|{h2:>23}')
    print('--------------------------------------------')
    for i in range(0, len(strs)):
        print(f'{strs[i]:<20}|{ints[i]:>23}')
    print()

def print_hist(t, h1, h2, strs, ints):
    for i in range(0, len(strs)):
        stars = '*' * ints[i]
        print(f'{strs[i]:>20} {stars}')
    print('\n')

title = input("Enter a title for the data:\n")
print(f'You entered: {title}\n')

header1 = input('Enter the column 1 header:\n')
print(f'You entered: {header1}\n')

header2 = input('Enter the column 2 header:\n')
print(f'You entered: {header2}\n')

strings = []
ints = []

data = input('Enter a data point (-1 to stop input):\n')
while data != '-1':
    if ',' not in data:
        print('Error: No comma in string.\n')
        data = input('Enter a data point (-1 to stop input):\n')
        continue
    elif data.count(',') > 1:
        print('Error: Too many commas in input.\n')
        data = input('Enter a data point (-1 to stop input):\n')
        continue
    data_s, data_i = data.split(',')
    data_s = data_s.strip()
    data_i = data_i.strip()

    if not data_i.isdigit():
        print('Error: Comma not followed by an integer.\n')
        data = input('Enter a data point (-1 to stop input):\n')
        continue

    strings.append(data_s.strip())
    ints.append(int(data_i))
    print(f'Data string: {data_s}')
    print(f'Data integer: {data_i}')
    print()
    data = input('Enter a data point (-1 to stop input):\n')

print_table(title, header1, header2, strings, ints)
print_hist(title, header1, header2, strings, ints)