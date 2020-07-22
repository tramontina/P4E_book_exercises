fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox.txt"
file = open(fname)
summ = 0
count = 0

import re
for line in file:
	line = line.rstrip()
	x = re.findall('^New Revision: ([0-9]+)', line) #find lew line start with New and numbers+
	if len(x) < 1 : 
		continue
	count = count +1
	print (x)

	for numbers in x:
		summ = summ + int(numbers)
		print (summ)

print (int(summ/count))


