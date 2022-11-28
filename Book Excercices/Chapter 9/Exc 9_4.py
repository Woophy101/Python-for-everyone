fs=input("Enter file name:")
fh=open(fs)
count=dict()
maxemail=None
maxnum=None
for lines in fh:
    if "From" not in lines: continue
    if "From:" in lines: continue #Con estos dos condicionales ya solo selecciono lineas con correos electonicos
    words=lines.split() #por lo tanto desde acá solo selecciono la segunda palabra de la linea y hago el dictionary
    if len(words)<2: continue #Guardian test. Esta a emedio hacer porque solo checjea que la linea tenga 3 palabras, creo yo que con los otros if statment no es necesario indagar mucho mas
    email=words[1] #Falta agregar el "Guardian", con el archivo mbox.txt tira traceback
    count[email]=count.get(email,0)+1
for email,num in count.items():
    if maxnum== None or num > maxnum:
        maxnum=num
        maxemail=email

print("The email:",maxemail,"has the most message send with",maxnum,"emails")

#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dictionary
#has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195
