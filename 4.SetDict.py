roll=set()
while(True):
    r=int(input("Enter the RollNo : "))
    roll.add(r)
    ch=int(input("Enter 1 to Add One More : "))
    if(ch!=1):
        break

course =dict()
CName = input("Enter a Course Name : ")
course.update({"Cname": CName})
Cdur = input("Enter a Course Duration : ")
course.update({"Duration": Cdur})
course.update({"RollNo": roll})

print(course)
