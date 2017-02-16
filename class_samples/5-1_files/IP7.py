
 
print("Welcome to the Haiku Generator!") 
print("Provide your first line of your Haiku:") 
line_1 = str(raw_input()) 
print("Provide your second line of your Haiku:") 
line_2 = str(raw_input()) 
print("Provide your thrid line of your Haiku:")
line_3 = str(raw_input()) 
print("Which file would you like to put your Haiku??")
title = raw_input()
my_file = open(title, "w")

my_file = (line_1 + "\n")
my_file = (my_file + line_2 + "\n")
my_file = (my_file + line_3)

print(my_file)
