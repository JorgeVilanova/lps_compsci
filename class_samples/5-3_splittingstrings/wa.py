walking_file = open("walking_instructions.txt", "r")

lineToPrint = walking_file.readline()
#this is using a while loop in order to tell that when there are only characters and not a blank space, to continue the loop. It will stop when there is no more text.
while lineToPrint != "":
	print(lineToPrint + ", duh")
#This part will make the loop repeat itself in order to let the function know that there is more words to go.
	lineToPrint = walking_file.readline()
walking_file.close()
