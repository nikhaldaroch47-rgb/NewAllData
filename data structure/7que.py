# l = []
# for i in range(0,21):
#      l.append(i)
#      if i%2==0:
#         print("even")
#      else:
#         print("odd")

numbers = range(0,21)

result = ["even" if i%2==0 else "odd" for i in numbers]

print(result)
