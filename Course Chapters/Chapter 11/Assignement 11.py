import re

fh=open('regex_sum_1550957.txt')

snum=list()
for lines in fh:
    line=lines.rstrip()
    if re.findall('[0-9]+',line):
        snum.append(re.findall('[0-9]+',line))

inum=list()
sum=0
for numbers in snum:
    for number in numbers:
        inum.append(int(number))
        sum=sum+int(number)

print('Total sum', sum)


#print(snum)
