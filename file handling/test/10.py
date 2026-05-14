def list_(a):
    l = []
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True
print(list_([1,2,6,4,5,6,7]))


# l = [1,2,3,4,5,6]
# print(range(len(l)-1))  # this will print the index and simple len function will print the length of list 