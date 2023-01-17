a,b=input("Enter the Values Of A & B : ").split(" ")

#SWPPING TWO VALUES BY USING TEMP VARIABLE

def swaptemp(a,b):
    temp=a
    a=b
    b=temp
    return a,b

print("\nSWPPING WITH TEMPORARY VARIABLE\n")
print("Before Swapping A = {} and B = {}".format(a,b))
a,b=swaptemp(a,b)
print("After Swapping A = {} and B = {}".format(a,b))

#SWPPING TWO VALUES BY WITHOUT TEMP VARIABLE

def swap(a,b):
    a,b=b,a
    return a,b

print("\nSWPPING WITHOUT TEMPORARY VARIABLE\n")
print("Before Swapping A = {} and B = {}".format(a,b))
a,b=swap(a,b)
print("After Swapping A = {} and B = {}".format(a,b))
