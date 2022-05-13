max= None
min= None
count = 0
while True:
    snum=input("Enter numeric value:")
    if snum=="done":
        break
    try:
        fnum=float(snum)
        #print("Value:",fnum)
    except:
        print('Error: Value is not a number')
        continue
    if max==None:
        max=fnum
        #print("Max num value changed to",max)
    if min==None:
        min=fnum
        #print("Min num value changed to",min)

    if max<fnum:
        max=fnum
        print("new max is:",max)
    if min>fnum:
        min=fnum
        print("new min is:",min)
    count=count+1

print("Minimum:",min,"\nMaximum:",max,"\nNumber count:",count)






#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.
