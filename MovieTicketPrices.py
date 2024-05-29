'''
    Write a program that takes in a string that holds the values "day" or "night" and an integer that holds a person's
    age, and outputs a movie ticket price. Movie prices are free for everyone under the age of 4.
    Daytime prices are $8 for everyone age 4 or higher.
    Nighttime prices are
        $12 for ages 4 - 16,
        $15 for ages 17 - 54
        $13 for ages 55 and above.
'''

option = input('day/night: ')
age = int(input('age: '))
ticket_price = 0

if age < 4:
    ticket_price = 0
else:
    if option == 'day':
        ticket_price = 8
    elif option == 'night':
        if 4 <= age <= 16:
            ticket_price = 12
        elif 17 <= age <= 54:
            ticket_price = 15
        elif age >= 55:
            ticket_price = 13

if ticket_price == 0:
    print("Ticket Price: free")
else:
    print(f"Ticket Price: ${ticket_price}")