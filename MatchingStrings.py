str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
length = min(len(str1), len(str2))

count = 0

if str1 == str2:
    print("All characters match")
else:
    for i in range(length):
        if str1[i] == str2[i]:
            count += 1
if count == 1:
    print(f'{count} character matches')
else:
    print(f'{count} characters match')
