# print the sum of numbers present at even index 

l = [1,2,3,4,5,6,7,8,9,10]
a = 0


for i in l:
    if i%2!=0:
        a+=i
print(a)