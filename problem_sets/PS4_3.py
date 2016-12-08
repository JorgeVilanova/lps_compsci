list = []
print("Welcome to PumaPix, a parody of Netlix.")
print("Please enter your favorite shows.")
print("When done, input done.")
x = 1
while x <= 100000:
	print("Favorite Show:")
	f = raw_input()
	list.append(f)
	x = x + 1
	if f == "done":
		list.remove("done")
		break
x = 1
while x <= 5:
	for show in list:
		print(str(x) + ". " + show)
		x = x + 1
print("We've added some new shows that are pretty good.")
z = 1
list.append("Breaking Bad")
list.append("The Wire")
list.sort()
while z <= 5:
	for show in list:
		print(str(z) + ". " + show)
		z = z + 1
print("Thanks for using PumaPix, Please rate and donate because we are becoming bankrupt.")
