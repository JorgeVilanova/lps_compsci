#makes an empty dictionary so I can put info in here
myContacts = {}
#Just so it can go back to the beginning of the code
keepRunning = True
while keepRunning: 
	print("(0) Exit the code:")
	print("(1) Add phone number:")
	print("(2) Print full list of Contacts:")
	print("(3) Enter a name to retrieve that contact's phone number:")
	x = raw_input()
	if x == "0": 
		keepRunning = False
	elif x == "1":
		print("What is the name of the person?")
		y = raw_input()
		print("What is the phone number of this person?")
		z = raw_input()
#I put the raw inputs of y and z into this just so that the computer knows what to put into it
		myContacts[y] = z
	elif x == "2":
		print(myContacts)
	elif x == "3":
		print("Which contact would you like to aks for?")
		a = raw_input()
#From the launch this morning, I put the raw input of a which is the contact we are searching for and plug it into the myContacts variable in order to get the number associated with that name
		print(str(myContacts[a]))
