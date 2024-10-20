#WAP to check if a set of brackets is valid or not (every bracket closes later in the set)

a = str(input("Enter the set of brackets "))
l = len(a)
c=0
for i in range (l):
    if(a[i]=="("):
        c+=1
    elif (a[i]==")"):
        c-=1
        if(c<0):
            print("It is not a valid set of brackets")
            break
if(c==0):
    print("It is a valid set of brackets")
elif(c>0):
    print("It is not a valid set of brackets")