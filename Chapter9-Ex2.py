file = open("mbox-short.txt")
dictionary_day = {}
for line in file:
	if not line.startswith('From '):
		continue
	words = line.split()
	day = words[2]
	print (day)

	if day not in dictionary_day:
		dictionary_day[day] = 1
	else:
		dictionary_day[day] = dictionary_day[day] +1

print(dictionary_day)

