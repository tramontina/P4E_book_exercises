count = 0
total = 0

while True:
    num = input("Enter a number: ")
    if num == "done" :
    	break
    try:
        numb = int(num)
    except:
        print('Invalid input')
        continue
    total = total + numb
    count = count +1

print("Total", total, "Count", count, "Avarage", total/count)
