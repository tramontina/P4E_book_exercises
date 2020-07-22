file = open("mbox-short.txt")
dictionary_email = {}
for line in file:
	if not line.startswith('From '):
		continue
	words = line.split()
	email = words[1]
	print (email)

	if email not in dictionary_email:
		dictionary_email[email] = 1
	else:
		dictionary_email[email] = dictionary_email[email] +1

print(dictionary_email)
