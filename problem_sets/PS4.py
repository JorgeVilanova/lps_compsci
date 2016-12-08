#problem 1(a) of the problem set
account_balance = 1000
 
withdrawal = 50
 
while account_balance > 0:
        print("Ok, your withdrawal has been made.")
        print("Your balance is now $" + str(account_balance - withdrawal) + ".")
	account_balance = account_balance - withdrawal

#problem 1(b) of the problem set
bacteria_population = 1
minutes = 0 
while bacteria_population < 5000000:
        print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
        print("No need to disinfect the sink yet.")
        bacteria_population = bacteria_population * 2
        minutes = minutes + 1
print("After " + str(minutes) + " minutes, there are " + str(bacteria_population) + " bacteria in the sink.")
print("You shoud use some Clorox on the sink now.")


#Problem #2 of the problem set
#put this line at the start of your program
#to make the functions of this package available
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

#problem #3 of the problem set
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
