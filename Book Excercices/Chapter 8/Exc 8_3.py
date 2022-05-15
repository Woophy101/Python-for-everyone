#Exercise 3: Rewrite the guardian code in the above example without
#two if statements. Instead, use a compound logical expression using
#the or logical operator with a single if statement.

fname=input("Enter file name:")
fhand = open(fname)
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 or words[0]!="From": continue #Doble condicional para el if
    if len(words)>2:
        print(words[2])
