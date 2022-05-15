#Exercise 4: Find all unique words in a file
#hakespeare used over 20,000 words in his works. But how would you
#determine that? How would you produce the list of all the words that
#Shakespeare used? Would you download all his work, read it and track
#all unique words by hand?
#Let’s use Python to achieve that instead. List all unique words, sorted
#in alphabetical order, that are stored in a file romeo.txt containing a
#subset of Shakespeare’s work.
#To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
#Create a list of unique words, which will contain the final result. Write
#a program to open the file romeo.txt and read it line by line. For each

fname=input("Enter file name:")
fh=open(fname)
lst=list()
for lines in fh:
    words=lines.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)
