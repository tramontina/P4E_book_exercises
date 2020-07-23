fname = input("Enter file:")

if fname == "1" : fname = "mbox.txt" 
elif  fname == "2" : fname = "mbox-short.txt"
else : quit()

doc = open(fname)

di = dict()
for line in doc:
	if not line.startswith('From '):
		continue
	words = line.split()
	email = words[1]
	di[email] = di.get(email,0)+1
#print(di)

largest = 0
email = None
for key,value in  di.items():
	#print (key,value)
	if value > largest : 
		largest = value
		email = key
print(email, largest)
