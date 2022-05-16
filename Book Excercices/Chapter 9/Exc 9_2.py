#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).
#Sample Line:

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Sample Execution:

#python dow.py

#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}
fs=input("Enter file name:")
fh=open(fs)
days=list(("Mon","Tue","Wed","Thu","Fri","Sat","Sun"))
count=dict()
for lines in fh:
    if "From" not in lines: continue
    if "From:" in lines: continue
    words=lines.split()
    for word in words:
        if word in days:
            count[word]=count.get(word,0)+1

print(count)
