list = []
print("Welcome to PumaPix, a parody of Netlix.")
print("Please enter your favorite 5 shows.")
x = 1
while x <= 5:
	print("Favorite Show:")
	list.append(raw_input())
	x = x + 1
y = 1
while y <= 5:
	for show in list:
		print(str(y) + ". " + show)
		y = y + 1
print("We've added some new shows that are pretty good.")
z = 1
list.append("Breaking Bad")
list.append("The Wire")
list.sort()
while z <= 5:
	for show in list:
		print(str(z) + ". " + show)
		z = z + 1
