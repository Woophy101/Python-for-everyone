#Exercise 6: Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes.

#Enter a number: 6
#Enter a number: 2
#Enter a number: 9
#Enter a number: 3
#Enter a number: 5
#Enter a number: done
#Maximum: 9.0
#Minimum: 2.0
exits=list(["Done","done","finish","exit","stop","Stop"])
numbers=list()
while True:

    inps=input("Enter a numeric value:")
    if inps in exits:
        break
    try:
        inpf=float(inps)
    except:
        print("ERROR: Not a numeric value!")
        continue
    numbers.append(inpf)
print("The max value is:",max(numbers))
print("The min value is:",min(numbers))
