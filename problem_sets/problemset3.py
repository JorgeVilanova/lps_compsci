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
choice_2 = str(raw_input())
print("Choose Yes or No.") 
if choice_2 == "yes" or choice_2 == "Yes"
	print("Great Soldier I say!")
if choice_2 == "no" or choice_2 == "No"
	print("Cmon young lad, you will have fun, so come with us!")
print("As you escort the king with his royal army, you find another army getting ready for an ambush, you must choose which way is best to avoid the amry andsurvive with more people.") 
print("Which way shall we go sir? Left or Right?") 
ambush = raw_input()
if ambush is "left" or ambush is "Left"
	print("Well it seems that we have to go fight the army, lets hope we are strong enough.")
if luck <= 6:
	print("10 people were lost in the battle sir.  We only have another 10 left.")
if luck > 6:
	print("We didn't have any casualties, it seems as if we got lucky today.") 
if health < 5:
	print("Sir you need medical assistance, it seems as if you are bleeding to death!")
if health >= 5:
	print(str(name) + "  you barely have any scratches you are pretty durable.")
if strength < 6:
	print("Cmon we have to keep going, you're not strong but you have to continue")
if strength >= 6:
	print("Great we can continue on without any troubles.  Congrats we are almost there.")
print("We only have a mile left to go.  I think the money will be worth it.") 
print("We need a sacrifice to be made now, what will you want to sacrifice. Leave the Bishop, or a Soldiers?")
choice = str(raw_input())
if choice == "Bishop" or choice == "bishop":
	print("I know we have to always be with god but this time we have to be alone.")
print("We have made it good job, here is your money. " + str(money) + " Dollars.")
if choice == "Soldier" or choice == "soldier":
	print("I am sorry but you have served for the right cause, we will see you in the kingdom above young brave soldier.  May God be with you.")
if choice == "Neither" or choice == "neither":
	print("If you say so, there will be a bigger cash pay out. We really don't want you to go into the trouble of it but if we have to, we will need to.")
cash = int(money) * 10
print("You've made it to the end.  Here is your total cash. " + str(cash) + " , I hope you are happy with your payout.")
print("If you have made it to the end, Congrats! You can either try out all of the options to make a different story possible.  Or you can put in your credit or debit card information to play the full game.")
print("Just, Kidding, hope you've had fun") 
