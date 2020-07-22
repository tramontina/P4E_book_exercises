#insert file
fname = input("Enter file:")

#open file
if len(fname) < 1 : fname = "mbox-short.txt"
doc = open(fname)

#read file
doc2 = doc.read()

#print all content in upper case
x = doc2.upper()
print (x)
	
