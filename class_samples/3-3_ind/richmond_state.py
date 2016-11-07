print("How far do you live from Richmond State, in miles?") 
miles = int(raw_input())
if miles <= 30:
	print("Well we can see if you can get into this easily.")
elif miles > 30 and miles < 99:
	print("Well we will see if you are eligible.")
else:
	print("Ah hell nah, you hella far away.")
print("How about your GPA?")
gpa = float(raw_input())
if gpa >= 2.0 and gpa < 3.0:
	print("OK this will make it easier to get in dude.")
elif gpa < 2.0 and gpa > 1.0:
	print("Dang dude, sorry, we can't accept you.")
elif gpa >= 3.0 and gpa <= 5.0:
	print("Alright dude that's pretty good, you're really smart.")
elif gpa < 1.0:
	print("Boi, you stupid, why you applying.")
else:
	print("What the hell kind of gpa do you have?")
print("Now we will look at ACT scores.")
score = int(raw_input())
if score == 18: 
	print("Ok this is the bare minimum but it will do.")
elif score > 18 and score <= 32: 
	print("Alright this is good, you are doing good.")
elif score < 18:
	print("Sorry, we can't accept you into this school.")
else: 
	print("You are lying with your score, we can't rely on your application.")
print("Now we will see if you really want to go to this school.")
if miles <= 30 and gpa >= 2.0 and score >= 18:
	print("You're accepted to Richmond State University, Congrats!")
elif miles > 30 and gpa < 2.0 and score < 18:
	print("We are sorry to declare that you have not been admitted to the school.  Sorry.")
elif miles > 30 and gpa >= 2.5 and score > 18:
	print("You're accepted to Richmond State University, Congrats!")
elif miles > 30 and gpa < 2.5 and score < 18:
	print("We are sorry to declare that you have not been admitted to the school.  Sorry.")
else:
	print("We are sorry to declare that you have not been admitted to the school.  Sorry.")
