#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary

fs=input("File name:")
fh=open(fs)
days=list(("Mon","Tue","Wed","Thu","Fri","Sat","Sun"))
count=dict()
for lines in fh:
    words=lines.split()
    for word in words:
        if word in days:
            print(words)
            count[word]=count.get(word,0)+1
print(count)
