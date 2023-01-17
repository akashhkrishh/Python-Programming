alist=[14,44,24,422,2]

try:
    print("List ",alist)
    ch=int(input("Enter a Index Number : "))
    print("The List[{}] is {}".format(ch,alist[ch]))
except:
    print("The Index Number is Out of Range")
    last=len(alist)-1
    print("The Last Index is {} and List[{}] is {}".format(last,last,alist[last]))
else:
    print("No Errors Occurs")
finally:
    print("The Program End !")