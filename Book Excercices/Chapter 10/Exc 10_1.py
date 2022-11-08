while True:
    fstring=input("Enter file name:")
    try:
        fh=open(fstring)
        break
    except:
        print("Invalid filename")
        continue

count=dict()

for lines in fh:
    if "From" not in lines:
        continue
    if "From:" in lines:
        continue
    words=lines.split()
    if len(words)<2: continue
    for word in words:
        email=words[1]
        count[email]=count.get(email,0)+1

lst=list()
for k,v in list(count.items()):
    lst.append((v,k))

lst.sort(reverse=True)
for k,v in lst[:1]:
    print("the adress",v,"has send",k,"messages")




#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195
