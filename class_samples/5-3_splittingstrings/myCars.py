#Honda Civic 2013 Green
#Kia Sportage 2008 Blue
#Mercedes S550 2016 Silver


# a program for keeping track of used cars
# problem designed by mflax@leadps.org
 
# represents a single car
class Car(object):
    # every car has a make, model, year, and color
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
 
    # prints the ad for this car to the terminal
    def ad(self):
        print("Buy this beautiful " + self.color + " " + str(self.year) + " " + self.make + " " +self.model + "!")
 
 
# takes a list of Car objects and prints the ad for all of them
def printAds(carList):
    for c in carList:
        c.ad()
 
# THE loadCars FUNCTION IS FOR YOU AND YOUR PARTNER TO IMPLEMENT
# takes a list to fill with Car objects and a filename for saved Cars
# opens the file, creates new Car objects and adds them to the list
 
# note that you can pass a list and that the things you add to it will be there after calling this function
# this isn't true in every language!!
def loadCars(carList, filename):
    # open the file
	y = open(filename, "r")
    # read each line from the file
	line = y.readline()

    # for each one, pull apart the variables to create a Car object
#This will make the function start to read each line specifically. 	
	while line != "":
#splits the texts in each line
		lineSplit = line.split()
#This will append the types in the file for each part of the list
		ourCars.append(Car(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3]))
#this will get the specifical words in the line to match it. There is a better function right above
#		print("Buy this beautiful " + lineSplit[3] + " " + lineSplit[2] + " " + lineSplit[0] + " " + lineSplit[1] + ".")
#this will make it read again so that it can continue until it has nothing left to read
		line = y.readline()
    # close the file
#	y.close() 

 
 
 
# execution starts here!
 
# here's an empty list that we'll fill with cars
ourCars = []

# we'll add this car to start as an example of adding a car to our list
ourCars.append(Car("Honda", "Fit", 2009, "Grey"))
 
# here you load the list of cars
print("Hey user, what's the filename of your car list?")
name = raw_input()
loadCars(ourCars, name)
 
# now we'll walk through the list
printAds(ourCars)

