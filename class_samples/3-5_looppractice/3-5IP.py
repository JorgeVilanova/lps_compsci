print("What numbers would you like the multiples for?")
num = float(raw_input())
multiple = float(0)
while num < float(1000.0):
	total = multiple * num
	print(str(multiple) + " times " + str(num) + " equals " + str(total))
	multiple = multiple + 1
	if total >= 1000:
		print("Thats all the multiples for " + str(num) + " Thank you and have a nice day.")
		break
