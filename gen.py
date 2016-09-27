def mystery(x):
    for i in range(x):
        yield(i**2)

for i in mystery(5):
    print(i, end=" ")
print("")
