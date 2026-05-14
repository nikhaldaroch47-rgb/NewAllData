a = input("enter a string : ")

if len(a)<3:
    print("invalid string ")
elif len(a)<=3:
    print(a[:]+"ing")
else:
    print(a[:]+"ly")