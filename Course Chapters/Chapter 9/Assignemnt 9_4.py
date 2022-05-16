#9.4 Write a program to read through the mbox-short.txt and figure out who has
#sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file. After the
#dictionary is produced, the program reads through the dictionary using a
#maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=dict()
maxemail=None
maxnum=None
for lines in handle:
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

print(maxemail,maxnum)
