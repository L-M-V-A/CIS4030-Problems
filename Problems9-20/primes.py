num = 20
count = 0
prime = True
output = ""
while(count < 10):
	prime = True
	for i in range(2, num):
		if num % i == 0:
			prime = False
			break
	if prime:
		count = count + 1
		output = output + str(num) + " "
	num = num + 1

print(output)
