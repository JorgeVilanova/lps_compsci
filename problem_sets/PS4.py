#account_balance = 1000
 
#withdrawal = 50
 
#while account_balance > 0:
 #       print("Ok, your withdrawal has been made.")
  #      print("Your balance is now $" + str(account_balance - withdrawal) + ".")
#	account_balance = account_balance - withdrawal
#bacteria_population = 1
#minutes = 0
 
#while bacteria_population < 5000000:
 #       print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
  #      print("No need to disinfect the sink yet.")
   #     bacteria_population = bacteria_population * 2
    #    minutes = minutes + 1
 
#print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
#print("You shoud use some Clorox on the sink now.")
# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)
print("Here take a guess at what the number could be from 1 to 1000?")
guess = -1
takes = 0
print(myNum)
while guess != myNum:
	guess = int(raw_input())
	if guess > myNum:
		print("Too High, try again bud!")
		takes = takes + 1
 	if guess < myNum:
		print("Too Low, Continue trying!")
		takes = takes + 1
	if guess == myNum:
		print("Congrats, you win dude!!! And it only took you " + str(takes) + " tries.")


