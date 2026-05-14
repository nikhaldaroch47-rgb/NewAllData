logs = {"404":[10, 12, 15, 20],"500":[12,20,22,25],"403":[10,20,30]}

# print(logs)
# set_404 = set(logs["404"])
# set_500 = set(logs["500"])
# set_403 = set(logs["403"])

# s = {i for i in set_404 & set_500 & set_403}
# print(s)

# s = {i for i in set_404.difference(set_500)}
# print(s)

s = {i for i in  logs["403"] if i in logs["404"] and i in logs["500"] }
print(s)