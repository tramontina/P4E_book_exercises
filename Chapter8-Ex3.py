fhand = input("Digite o nome do arquivo: ")
if len(fhand) < 1 : fhand = "mbox-short.txt"
xhand = open(fhand)

for line in xhand:
	words = line.split()
	#print ("Debug", words)
	if len(words) == 0 or words[0] != "From" : continue
	print (words[2])

