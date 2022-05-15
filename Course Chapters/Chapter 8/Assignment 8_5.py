#8.5 Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in
#the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#Also look at the last line of the sample output to see how to print the count.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
n = 0
lst=list()

for lines in fh:
    if lines.startswith("From"):
        if not lines.startswith("From:"):
            words=lines.split()
            lst.append(words[1])
            print(words[1])
            n=n+1
print("There were", n, "lines in the file with From as the first word")

#print(lst)  No se usa este print list porque se tiene que hacer print de la linea para evitar los corchetes

#No es buena idea usar if words[0] == "From": Porque en el casod e que la linea tenga len()=0 da un error.
#Se recomienda usar un "Guardian" del tipo:

#if len(words)<1:           if line == "":
#    continue                   continue
#if words[0]=="From:":      if words[0]=="From":
#    bla bla bla                vla vla vla

#En este caso el primer If actua como una especie de "try" y evita generar un array vacio.

#En la revisión usan el siguiente loop para checkear si la linea cumple con las condiciones para ser guardada;

for lines in fh
    line.rstrip()
    if len(words)<1:
        continue #Guardian
    if words[0] != "From"
        continue #si la linea no comienza con "From" comienza el for-loop con el siguiente item en la lista
    lst.append() #Luego acá se comienza a guardar los strings en la lista que correspodne
