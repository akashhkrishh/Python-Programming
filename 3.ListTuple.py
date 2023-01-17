subject = ('DB','DS','OOSE','CC')
marks=[]

for i in range(0,len(subject)):
    #print(subject[i])
    mark=int(input("Enter the Mark {} : ".format(subject[i])))
    marks.append(mark)

print("Total : {} / {}".format(sum(marks),len(marks)*100))
print("Average : {} / 100 ".format(sum(marks)/len(marks)))