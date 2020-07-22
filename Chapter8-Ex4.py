fhand = input("Enter file: ")
if len(fhand) < 1 : fhand = "romeo.txt"

xhand = open(fhand)
lista = []

for line in xhand :
	words = line.split()
	#print (words, "______")

	for word in words:
		if word in lista:
			continue
		lista.append(word)
		#print (lista)

print (sorted(lista))
