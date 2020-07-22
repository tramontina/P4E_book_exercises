import string
import re


# Initialize variables
dic = dict()


file = open("romeo-full.txt")

for line in file: 
	x = re.findall('[a-zA-Z]', line)
	if len(x) < 1 : 
		continue

	for letter in x:
		letter = letter.lower()
		if letter not in dic:
			dic[letter] = 1
		else:
			dic[letter] = dic[letter]+1

l = list()
for key, val in list(dic.items()):
    l.append((val, key))
l.sort(reverse=True)

for key, val in l:
	print (key, val)
