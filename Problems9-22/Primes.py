"""
Write a python code to check whether a given number is prime or not. If a
number is prime then it should print Prime and if the number is not prime
it should print Not Prime. Prime numbers are numbers that are only
divisible by 1 and itself. Make a note that 1 is not a prime number. This
program should terminate when the user gives an input as 0.
"""


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# main
while True:
    try:
        data = int(input("Enter a number, 0 to exit:"))
    except ValueError:
        print("Enter an integer number.")
        continue

    if not data:
        break
    elif data == 1 or data < 0:
        print("Not Prime")
        continue

    if is_prime(data):
        print("Prime")
    else:
        print("Not Prime")
