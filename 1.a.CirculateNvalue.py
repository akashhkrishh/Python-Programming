#CIRCULATE VALUES BY USING INDEX 

def circle(alist,order):
    for i in range(0,order):
        j=len(alist)-1
        while(j>0):
            temp=alist[j]
            alist[j]=alist[j-1]
            alist[j-1]=temp
            j=j-1
        print(i+1,'Rotation',alist)
        
alist=[1,2,3,4,5,6]
print('Given list',alist)
circle(alist,4) 

#CIRCULATE VALUES BY USING POP AND APPEND FUNCTION
 
def circle(alist,order):
    for i in range(0,order):
        val=alist.pop(0)
        alist.append(val)
        print(i+1,'Rotation',alist)

alist=[1,2,3,4,5,6]
print('Given list',alist)
circle(alist,4)

