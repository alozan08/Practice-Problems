'''
    define a function called exact_change that takes the total change amount in cents and calculates
    the change using the fewest coins
    The coin types are:
        pennies, nickels, dimes, and quarters
    Write a main program that reads the total change amount as an integer input, calls exact_change()
    and outputs the change, one coin per line. Use singular and plural coin names as appropriate.
        1 penny vs 2 pennies
    output 'no change' if the input is 0 or less
'''
def exact_change(total):
    quarters = total // 25
    total = total % 25

    dimes = total // 10
    total = total % 10

    nickels = total // 5
    total = total % 5

    pennies = total

    return pennies, nickels, dimes, quarters


if __name__ == '__main__':
    total = int(input())
    change = exact_change(total)
    labels_plural = ['pennies', 'nickels', 'dimes', 'quarters']  # Order: smaller to larger
    labels_singular = ['penny', 'nickel', 'dime', 'quarter']
    count = 0
    if sum(change) == 0:
        print('no change')
    else:
        for i in range(4):
            if change[i] == 0:
                continue
            elif change[i] == 1:
                print(change[i], labels_singular[i])
            else:
                print(change[i], labels_plural[i])
            count += 1