import math

x1,y1=input("Enter the Values Of ( X1, Y1 ) : ").split(" ")
x2,y2=input("Enter the Values Of ( X2, Y2 ) : ").split(" ")
x1,x2,y1,y2=int(x1),int(x2),int(y1),int(y2)

#DISTANCE BETWEEN TWO POINTS

distance=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print("The Distance Between Two Points : {:0.2f} ".format(distance))
