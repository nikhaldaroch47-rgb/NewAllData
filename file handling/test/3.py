
def letter(l):
    upper_count = 0
    lower_count = 0
    for i in l:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return lower_count,upper_count
count = letter("Nikhil")
print(count)



    