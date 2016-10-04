"""
Write a python code to print Armstrong number in a given interval. An
Armstrong number is a number that is equal to the sum of the cubes of
its own digits. For example 371 is an Armstrong number as
371 = 3*3*3 + 7*7*7 +1*1*1. The user will have to enter an interval and
the program should display all the Armstrong numbers within that
interval.The program should terminate when user gives the range as 0.
"""


#def is_armstrong(number):
#    total = 0
#    for digit in number:
#        total += int(digit)**3

#    if total == int(number):
#        return True
#    else:
#        return False
#    if number == str(sum(int(x)**len(number) for x in number)):
#        print(number)


# main
while True:
    try:
        range_start = int(input(
                '''Enter the start of your interval, 0 to exit: '''))
        if range_start == 0:
            break
        range_end = int(input("Enter end of your interval:"))
    except ValueError:
        print("Enter an integer number.")
        continue

    if range_start < 0 or range_end < 0:
        print("Enter positive integers for your interval.")
        continue
    if range_end < range_start:
        print("Enter an interval where end > start.")
        continue
    L = []
    L.clear()
    for i in range(range_start, range_end + 1):
        number = str(i)
        if i == sum(int(x)**len(number) for x in number):
            L.append(i)
    print(L)
