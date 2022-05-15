#7.2 Write a program that prompts for a file name, then opens that file and
#reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the
#lines and compute the average of those values and produce an output as shown
#below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tconf=0
n=0
for line in fh:
    if "X-DSPAM-Confidence:" in line:
        npos=line.find(':')
        line=line.rstrip()
        confvalue=line[(npos+1):]
        fconf=float(confvalue)
        tconf=tconf+fconf
        n=n+1
avconf=tconf/n
print("Average spam confidence:",avconf)
