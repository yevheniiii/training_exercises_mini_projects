# Exercise 1

s = "abcdefghu"

for items in range(len(s)):
    if s[items] == 'i' or s[items] == 'u':
        print("There is an i or u")

for item in s:
    if item == 'i' or item == 'u':
        print("There is an i or u")

############################################################################

# Exercise 2

an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1

print("What does that spell?")
for i in range(times):
    print(word, "!!!")

############################################################################

#Exercise 3

# Find the greatest common divisor of two positive integers — the largest
# integer that divides each of them without remainder.


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)


print(gcdRecur(5, 17))

############################################################################

# In recursive way

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


print(gcdIter(20, 15))

############################################################################

# Exercise 4
# Write a program to calculate the credit card balance for each month if a person only pays the minimum monthly payment
# required by the credit card company each month.

balance = 484

annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

monthlyPaymentRate = 0.04

minMonPay = monthlyPaymentRate * balance
monUnpaidBal = balance - minMonPay
remainingBal = monUnpaidBal + (monthlyInterestRate * monUnpaidBal)
print("Remaining balance: " + format(remainingBal, '.2f'))


def calc(remainingBal):
    iter = 0
    while iter < 11:
        minMonPay = monthlyPaymentRate * remainingBal
        monUnpaidBal = remainingBal - minMonPay
        remainingBal = monUnpaidBal + (monthlyInterestRate * monUnpaidBal)
        print("Remaining balance: " + format(remainingBal, '.2f'))
        iter += 1
    return format(remainingBal, '.2f')

print(calc(remainingBal))