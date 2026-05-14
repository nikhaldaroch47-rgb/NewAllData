'''n = 5
fact = 1
for i in range(1,n+1):
    fact*=i
print(f"factorial of 5 is {fact}")'''
# 2
'''word = "programming"
char_count = {}
for i in word:
    if i in char_count:
        char_count[i]+=1
    else:char_count[i]=1  
for char , count in char_count.items():
    print(char + ":" , count) '''

# pattern prob
 
'''for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print() '''  

# 4 
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()       
               
        