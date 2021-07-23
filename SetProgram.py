###########Set##############
##Unordered and Unchangeable

thisset = {"red","orange","white","purple","violet"}

print(thisset)

print("++++++++++to access data using loop+++++++++++")
for x in thisset:
    print(x)

print("++++++++++to check a element exists or not+++++++++++")
print("red" in thisset)


print("++++++++++to add an element+++++++++++")
thisset.add("orange")
print(thisset)


print("++++++++++to remove an element+++++++++++")
thisset.remove("orange")
thisset.pop()
print(thisset)

print("++++++++++joining in set+++++++++++")
