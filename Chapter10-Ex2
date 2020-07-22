name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
lst = list()

for line in handle:
    if not line.startswith('From '):
    	continue
    words = line.split()
    word = words[5]
    spl = word.split(':')    
    time = spl[0]

    if time not in di:
        di[time] = 1
    else:
        di[time] = di[time]+1
    print (di)

for key, val in  di.items()  :
    temp = (key, val)
    lst.append(temp)
    lst = sorted(lst)
for key, val in lst :
	print (key, val)
    
