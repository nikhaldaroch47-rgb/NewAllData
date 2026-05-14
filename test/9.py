names = ["a","b","c","d"]

scores = [45,78,90,60]
for i,(j,k)  in enumerate(zip(names,scores)):
    print(f"{i} -> {j} scored {k}")


