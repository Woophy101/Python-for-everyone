def chop(x):
    x.remove(0)
    last=len(x)
    x.remove(last)
    return(lst)

def mid(x):
    last=len(x)
    ilast=int(last) -1
    newlst=list()
    newlst.append(x[0])
    newlst.append(x[ilast])
    return(newlst)

lst=list(range(0,5))
print(lst)
chopped=chop(lst)
print("Chopped:",chopped)
middle=mid(lst)
print("Middled:",middle)

#Exercise 1: Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.
