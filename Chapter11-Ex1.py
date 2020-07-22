import re

user_input = input("Enter a regular expression you would like to count? ")
count = 0

file = open("mbox.txt")
for line in  file:
	line = line.rstrip()
	if re.search(user_input, line) :
		count = count+1
		print (line)
		print (count)

print ("mbox.txt had", str(count), "lines that mached", user_input, ".")
