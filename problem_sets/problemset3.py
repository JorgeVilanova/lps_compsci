print("What will your characters name be on this wonderful journey?")
name = raw_input()
print("You are on a wonderful and amazing journey in the world of Whiterun.  As you enter the town you have a choice of your character.")
print("You may choose your Health, Strength, and Luck.  May the dragons be with you!")
print("Health")
health = int(raw_input())
print("Strength")
strength = int(raw_input())
print("Luck")
luck = int(raw_input())
if health + strength + luck > 15:
	print("Please hold back on your powers, we only need a couple things done.")
	health = 5
 	strength = 5 
	luck = 5
	print("Your Strength, Luck and Health will be set to 5.")
	print("Now that we are ready, we will start escorting our dragon king, how much money will you want for your escort.")
	money = raw_input()
	print("If anything comes up we will pay you extra or less.")
	print("There's a fork in the road, which way shall we go, left or right.")
	choice = raw_input()
	if choice == "right" or choice == "Right":
		print("There is a dragon that can be killed, your abilities can't get you through it this time. You died.")
	elif choice == "left" or choice == "Left":
		print("We can pass through this direction, we will surely make it to the town.")
	total = int(money) / 10	
	print("Thank you for what you have done, here is your money. " + str(total) + "  money was given to your account.") 

if health + strength + luck <= 15: 
	print("Alright young sir, are you sure you want to go on this dangerous quest?") 
choice = raw_input() 
if choice == "yes" or choice == "Yes":
	print("Well if you are so sure of yourself, how much currency would you want?")
money = int(raw_input())
if money <= 500:
	print("Well that seems like a reasonable price.")
if money > 500:
	print("No that will not be give, the maximum for your services will be paid with 500 dollars!")
print("Now with your basic training will you join us in escorting the king?")
print("As you escort the king with his royal army, you find another army getting ready for an ambush, you must choose which way is best to avoid the amry and survive with more people.")
print("Which way shall we go sir? Left or Right?")
ambush = raw_input()
if ambush is "left" or ambush is "Left":
	print("Well it seems that we have to go fight the army, lets hope we are strong enough.")
if luck <= 7:
	print("10 people were lost in the battle sir.  We only have another 10 left.")
if luck > 7:
	print("We didn't have any casualties, it seems as if we got lucky today.") 
if health < 7:
	print("Sir you need medical assistance, it seems as if you are bleeding to death!")
if health >= 7:
	print(str(name) + "  you barely have any scratches you are pretty durable.")
if strength < 6:
	print("Cmon we have to keep going, you're not strong but you have to continue")
if strength >= 6:
	print("Great we can continue on without any troubles.  Congrats we are almost there.")
 
