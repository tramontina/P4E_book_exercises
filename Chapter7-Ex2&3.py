fname = input("Enter file name: ")
try:
	if fname == 'na na boo boo':
		print('NA NA BOO BOO TO YOU - You have been punk\'d!')
		exit()
	fh = open(fname)
except:
	print ("File cannot be opened:", fname)
	exit()

count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    t = line.find(":")
    #print(t)
    number= float(line[t+1:])
    #print (number)
    
    count = count + 1
    total = total + number

average = total/count
print ("Average spam confidence:", average)
