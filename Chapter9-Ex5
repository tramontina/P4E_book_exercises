
file = open("mbox-short.txt")
di = {}

for line in file:
    if not line.startswith('From '):
    	continue
    words = line.split()
    word = words[1]
    spl = word.split('@')    
    #print (spl)
    domain = spl[1]

    if domain not in di:
    	di[domain] = 1
    else:
        di[domain] = di[domain]+1

print (di)
    
