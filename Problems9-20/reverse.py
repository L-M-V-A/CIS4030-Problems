output = ""
for i in range(1, 6):
	output = str(i) + " " + output
	print(output)
b = bytearray(output, "utf-8")
print(b) 
