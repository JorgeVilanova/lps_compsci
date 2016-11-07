print("How much does the nacho cost bauss?")
nacho_price = int(raw_input())
print("How much money do you have in your pocket?")
cash = int(raw_input())

if nacho_price > cash: 
	print("Sorry, you can't have nachos")
#bug is here, can be the same amount
if nacho_price <= cash:
	print("You can have nachos")
if nacho_price == cash:
	print("You are a lucky person.")
print("Thanks for buying my nachos, I need it for my spain trip.")
