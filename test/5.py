# Using enumerate(), print the index of all negative numbers in a list

l = [-1,-2,3,4,5,-6,-7,-8]

for i,j in enumerate(l):
    if j<0:
        print(i,end=" ")