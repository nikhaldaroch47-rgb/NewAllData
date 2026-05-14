a = input("enter a string : ")

if len(a)<2:
    print("invalid str")
else:
    print(a[:2]+a[-2:])