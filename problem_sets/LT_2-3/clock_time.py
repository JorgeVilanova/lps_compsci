print("What hour is it in New York?")
hour = raw_input() 
print("What minute is it in New York?")
min = raw_input()
cali = (int(hour) + 9) % 12
print("Then the time in New York will be " + str(hour) + ":" + str(min) + " but the time in california is " + str(cali) + ":" + str(min) + ".")
