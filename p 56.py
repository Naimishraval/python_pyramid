no=int(input("Enter rows limit=>"))
for i in range(1,no+1):
    for j in range(1,i+1):
        if i==1:
            print(chr(92),end=" ")
        if i==2:
            print(chr(39),end=" ")
        if i==3:
            print(chr(126),end=" ")
        if i==4:
            print(chr(61),end=" ")
        if i==5:
            print(chr(62),end=" ")
    print()