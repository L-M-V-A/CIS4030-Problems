from math import pow


def is_armstrong(number):
    digits = []
    for digit in number:
        digits.append(int(digit))

    if len(digits) < 2:
        return False

    total = 0
    for ints in digits:
        total += pow(ints, 3)

    if total == int(number):
        return True
    else:
        return False

while True:
    try:
        range_start = int(input("Enter the start of your interval, 0 to exit:"))
        if range_start == 0:
            break
        range_end = int(input("Enter end of your interval:"))
    except ValueError:
        print("Enter an integer number.")
        continue

    if range_start < 0 or range_end < 0:
        print("Enter positive integers, where start < end, for your interval.")

    for i in range(range_start, range_end + 1):
        if is_armstrong(str(i)):
            print(i)
