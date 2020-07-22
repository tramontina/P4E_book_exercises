lista = ["manga", "pepino", "tomate" ,"uva", "bolo"]

def chop(lst): 
	del lst[0]
	del lst[-1]

def middle(lst):
	new = lst[1:]
	del new[-1]
	return new

chop_list = chop(lista)
print (chop_list)
print (lista)

middle_list = middle(lista)
print (middle_list)
print (lista)
