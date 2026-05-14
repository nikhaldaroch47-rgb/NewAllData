a = ["today is very hot day","i am from punjab","i work in it company"]

# list_compheresion = [j for i in a for j in i.split() if len(j)<4]

# print(list_compheresion)
for i in a:
    for j in i.split():
        if len(j)<4:
            print(j,end=" ")




