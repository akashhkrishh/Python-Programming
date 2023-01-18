def letter():
    name=[]
    num = int(input("Enter the Number of Name :"))
    for i in range(0,num):
        n=input("Enter the Name :")
        name.append(n.capitalize())
    letter = input("Enter the Starting Letter of the Name :").upper()
    for i in range(0,len(name)):
        n=name[i]
        if(n[0]==letter):
            print(name[i])
