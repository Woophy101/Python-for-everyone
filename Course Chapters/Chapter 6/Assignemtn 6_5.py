#6.5 Write code using find() and string slicing (see section 6.10) to extract
#the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

#Find the number zero
npos = text.find('0')
print("Zero is at position",npos)

#Find the ":" (forma opcional, considera todo lo que viene despues como numero)
#npos = text.find(':')
#snum=text[npos+1:]

#Extract the numbers
snum=text[npos: ]

#Convert to float and print
fnum=float(snum)
print(fnum)
