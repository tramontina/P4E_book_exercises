h = input("Enter Hours: ")
try:
    h=float(h)
except:
    print("Not a number")
    quit()

r = float(input("Enter Rate: "))


def computepay():
    if h <=40 :
    	return (h*r)
    elif h > 40 :
        x = (h-40)*(r*1.5)+40*r
        return (x)

p = computepay()
print("Pay",p)
