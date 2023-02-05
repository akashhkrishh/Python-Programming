def add(a,b):
    print("\nAddition of {} + {} = {}\n".format(a,b,a+b))
def sub(a,b):
    print("\nSubraction of {} - {} = {}".format(a,b,a-b))
def mul(a,b):
    print("\nMultiplication of {} * {} = {}".format(a,b,a*b))
def div(a,b):
    print("\nDivision of {} / {} = {:0.2f}".format(a,b,a/b))

a,b = input("Enter the Values A and B :").split(" ")
a,b = int(a),int(b)
while(True):
    print("\nChoose the Option 1 to 4 :\n1.Addition \n2.Subraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("\nEnter the Choice : "))
    if(ch==1):
        add(a,b)
    elif(ch==2):
        sub(a,b)
    elif(ch==3):
        mul(a,b)
    elif(ch==4):
       div(a,b)
    elif(ch==5):
       break
    else:
        print("Invalid Choice !")
