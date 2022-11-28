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
    if "From" not in lines: continue
    if "From:" in lines: continue

    pos=lines.find(":")
    lines=lines.rstrip()
    hour=lines[(pos-2):(pos)]
    count[hour]=count.get(hour,0)+1

lst = list()
for key, val in list(count.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)




#Exercise 2: This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.
#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1
