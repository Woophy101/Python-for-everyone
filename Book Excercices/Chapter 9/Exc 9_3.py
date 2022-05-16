

fs=input("Enter file name:")
fh=open(fs)
count=dict()
for lines in fh:
    if "From" not in lines: continue
    if "From:" in lines: continue #Con estos dos condicionales ya solo selecciono lineas con correos electonicos
    words=lines.split() #por lo tanto desde acá solo selecciono la segunda palabra de la linea y hago el dictionary
    email=words[1] #Falta el "Guardian"
    count[email]=count.get(email,0)+1
print(count)

#Exercise 3: Write a program to read through a mail log, build a histogram
#using a dictionary to count how many messages have come from
#each email address, and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}
