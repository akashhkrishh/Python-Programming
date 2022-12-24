def rotate(l,order):
    for i in range(0,order):
        j=len(l)-1
        while j>0:
            temp=l[j]
            l[j]=l[j-1]
            l[j-1]=temp
            j=j-1
        print(i,'rotation',l)
    return

l=[1,2,3,4,5]
rotate(l,3)
