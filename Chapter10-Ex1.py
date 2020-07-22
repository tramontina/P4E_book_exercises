
file = input("Enter a file: ")

if file == "1" : file = "mbox.txt" 
elif  file == "2" : file = "mbox-short.txt"
else : quit()

fileo = open(file)
di = dict()

for line in fileo:
    if not line.startswith('From '):
    	continue
    words = line.split()
    word = words[1]
    #print (word)  

    if word not in di:
    	di[word] = 1
    else:
        di[word] = di[word]+1

#print (di)

l = list()
for key, val in list(di.items()):
    l.append((val, key))
l.sort(reverse=True)

for key, val in l[:1]:
    print(val, key)
    
