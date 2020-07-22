largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
    	break

    try:
        numb = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None :
    	largest = numb
    elif numb > largest :
   	 	largest = numb

    if smallest is None :
    	smallest = numb
    elif numb < smallest :
    	smallest = numb




print("Maximum is", largest)
print("Minimum is", smallest)
