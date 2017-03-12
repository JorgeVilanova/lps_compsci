class Player(object):
  	def __init__(self, name, age, jersey, position, goals):
		self.name = name
		self.age = age 
		self.jersey = jersey
		self.position = position
		self.goals = goals 
  	def getStats(self):
		summary = "Name: " + self.name + "\n"
		summary = summary + "Age: " + str(self.age) + "\n"
		summary = summary + "Jersey: " + str(self.jersey) + "\n"
		summary = summary + "Position: " + self.position + "\n"
		summary = summary + "Goals: " + str(self.goals)
		return summary
#do not indent since this is different from self
def saveTeam(playerList, filename):
#open file with w to write in the file
		file = open(filename, "w")
#put it for the list of players under the load team funciton
		for l in playerList: 
#add each single one in the list until it hits goals and then it goes into a new line for the next part of the list to write in the new file
			file.write(l.name + " " + str(l.age) + " " + str(l.jersey) + " " + l.position + " " + str(l.goals) + "\n")
		file.close()
def loadTeam(filename):
		pass
players = []
# x.getStats()
keepRunning = True 
while keepRunning:
	print("(1) Start with a new team")
	print("(2) Open a file for an existing team")
	print("(3) Exit Completely")
	x = raw_input()
	if x == "1":
		print("What file would you like to use?")
		file = raw_input()
	if x == "3":
		keepRunning = False
	while x == "2":
		print("(0) To add a player:")
		print("(1) To see the players stats:")
                print("(2) Save players info:")
                print("(3) To exit and delete information:")
                y = raw_input()
                if y == "0":
                        print("What is the name of the player?")
                        playerName = raw_input()
                        print("What is the age of the player?")
                        playerAge = raw_input()
                        print("What is the jersey number?")
                        playerJersey = raw_input()
                        print("What is the players position?")
                        playerPosition = raw_input()
                        print("How many goals did this player get?")
                        playerGoals = raw_input()
                        myPlayer = Player(playerName, playerAge, playerJersey, playerPosition, playerGoals)
                        players.append(myPlayer)
                elif y == "1":
                        for p in players:
                                print(p.getStats())
                elif y == "2":
                        print("Which file would you like to save it in?")
			filename = raw_input() 
			saveTeam(players, filename)
                if y == "3":
			x = int(x) + 1
                        	
