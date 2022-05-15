#5.2 Write a program that repeatedly prompts a user for integer numbers until
#the user enters 'done'. Once 'done' is entered, print out the largest and
#smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the
#number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    #Check if input is "Done"
    if num == "done":
        break

    #Check if input is a float
    try:
        fnum=int(num)
    except:
        print("Invalid input")
        continue

    #Check if fnum is None
    if largest== None:
        largest =fnum
    if smallest == None:
        smallest = fnum

    #Check for largest and smallest
    if smallest > fnum:
        smallest=fnum
    if largest < fnum:
        largest = fnum

    #Print the value
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
