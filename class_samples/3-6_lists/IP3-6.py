ice_cream = ["vanilla", "chocolate", "cookie dough", "chocolate chip", "cookies with cream"]
print("There are a couple flavors here right now " + str(ice_cream))
print("What would you like to put into the list?")
ice_cream.append(raw_input())
for cream in ice_cream:
	print(cream)
