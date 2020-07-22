score = (input("Enter your score between 0.0 and 1.0: "))

# recebe score; retorna sctring
def computergrade(aScore):
	if (aScore >= float(0.9)) and (aScore<= float(1.0)):
		return ("A")
	elif (aScore >= float(0.8)) and (aScore<= float(0.9)):
		return ("B")
	elif (aScore >= float(0.7)) and (aScore <= float(0.8)):
		return ("C")
	elif (aScore >= float(0.6)) and (aScore<= float(0.7)):
		return ("D")
	elif (aScore > float(0)) and (aScore<= float(0.6)):
		return ("F")
	return ("ERROR: Score out of range")


try:
	score = float(score)
	grade = computergrade(score)
	print(grade)

except: 
	print ("ERROR: not a valid input")
