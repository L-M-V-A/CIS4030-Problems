def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


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
