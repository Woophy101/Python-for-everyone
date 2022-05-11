#Exercise 1: Write a program to read through a file and print the contents
#of the file (line by line) all in upper case. Executing the program will
#look as follows:

#python shout.py

#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#SAT, 05 JAN 2008 09:14:16 -0500

#You can download the file from www.py4e.com/code3/mbox-short.txt

fs=open('mbox-short.txt')
fstring=fs.read().rstrip()


#Exercise 2: Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#90 CHAPTER 7. FILES
#values from these lines. When you reach the end of the file, print out
#the average spam confidence.

#Enter the file name: mbox.txt
#Average spam confidence: 0.894128046745
#Enter the file name: mbox-short.txt
#Average spam confidence: 0.750718518519

#Test your file on the mbox.txt and mbox-short.txt files

fname=input('File name:')
try:
    fs=open(fname)
except:
    print('file not found')
    quit()

for lines in fs:
    if search=="X-DSPAM-Confidence:":
        print(search)
