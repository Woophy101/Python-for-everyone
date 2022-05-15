total = 0
count = 0
average = 0

while True:
    snum=input("Enter numeric value:")
    #aqui checkea si se quiere terminar el loop, Break hace salir del "While"
    #y permite el print de los valores
    if snum=="done":
        break
    #Chekear si el valor de input es un float y asignar variable
    try:
        fnum=float(snum)
    except:
        print('Error: Value is not a number')
        continue

    total=total+fnum
    count= count +1
    average=total/count

print("Total:",total,"\nCount:", count,"\nAverage:", average)











#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.

#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333
