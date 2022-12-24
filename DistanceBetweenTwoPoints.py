import math
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    print('The value of dx is', dx)
    print('The value of dy is', dy)
    d= (dx**2 + dy**2)
    dist=math.sqrt(d)
    return dist
x1 = float(input('Enter the first Number: '))
x2 = float(input('Enter the Second Number: '))
y1 = float(input('Enter the third number: '))
y2 = float(input('Enter the forth number: '))
z=distance(x1,x2,y1,y2)
print('The distance between two points are', z)
