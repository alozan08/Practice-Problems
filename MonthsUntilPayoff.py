'''
    Write a program that reads a loan amount, payment amt,interest rate, and outputs the number of payments
    required until the loan is payed, interest is added to current balance before a payment is applied
    Ex:
        1000.0
        50.0
        0.03
        output is 31 payments

'''
loan_amount = float(input("Enter loan amount: "))
payment = float(input("Enter payment: "))
interest = float(input("Enter interest: "))

num_pymt = 0

while loan_amount >= 0:
    loan_amount = (loan_amount * interest) + loan_amount
    loan_amount -= payment
    num_pymt += 1

if num_pymt == 1:
    print(f'{num_pymt} payment')
else:
    print(f'{num_pymt} payments')