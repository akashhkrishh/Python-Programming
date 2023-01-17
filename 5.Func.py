def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a,b = input("Enter the Values A and B :").split(" ")
a,b = int(a),int(b)
while(True):
    print("\nChoose the Option 1 to 4 :\n1.Addition \n2.Subraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("\nEnter the Choice : "))
    if(ch==1):
        print("\nAddition of {} + {} = {}".format(a,b,add(a,b)))
    elif(ch==2):
        print("Subraction of {} - {} = {}".format(a,b,sub(a,b)))
    elif(ch==3):
        print("\nMultiplication of {} * {} = {}".format(a,b,mul(a,b)))
    elif(ch==4):
       print("\nDivision of {} / {} = {}".format(a,b,div(a,b)))
    elif(ch==5):
       break
    else:
        print("Invalid Choice !")
