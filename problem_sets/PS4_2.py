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
#Number 2 of the problem set and with challenge : 3
