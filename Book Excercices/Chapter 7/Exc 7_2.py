fname=input('File name:')
try:
    fs=open(fname)
except:
    print('file not found')
    quit()

tconf=0.0
n=0
for line in fs:
    if "X-DSPAM-Confidence:" in line:
        npos=line.find(':')
        line=line.rstrip()
        confvalue=line[(npos+1):]
        fconf=float(confvalue)
        tconf=tconf+fconf
        n=n+1
avconf=tconf/n
print(avconf)


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
