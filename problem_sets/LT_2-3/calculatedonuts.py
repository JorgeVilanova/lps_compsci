print("How many people will you have at your party?")
people = raw_input()

print("How many doughnuts will you have at your party?")
doughnuts = raw_input()

print("Our party has " + str(people) + " people and " + str(doughnuts) + " doughnuts!")

remainder = int(doughnuts) // int(people)
print("Each person in the party gets " + str(remainder) + " donuts")
