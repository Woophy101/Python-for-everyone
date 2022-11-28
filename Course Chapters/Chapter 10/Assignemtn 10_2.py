#10.2 Write a program to read through the mbox-short.txt and figure out the distribution
#by hour of the day for each of the messages. You can pull the hour out from the 'From '
#line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count=dict()

for lines in handle:
    if "From" not in lines: continue
    if "From:" in lines: continue
    words=lines.split()
    time=words[5].split(':')
    count[time[0]]=count.get(time[0],0)+1

tmp = list()
for key, val in list(count.items()):
    tmp.append((key, val))

tmp.sort()

for k,v in tmp:
    print(k,v)
