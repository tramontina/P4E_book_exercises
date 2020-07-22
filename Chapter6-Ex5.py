text = "X-DSPAM-Confidence:    0.8475";
y = len(text)
x = text.find('0.8475')
# print(float(text[x:y]))


ipos = text.find(':')
#print(ipos)
piece = text[ipos+2:]
value = float(piece)
print(value)
