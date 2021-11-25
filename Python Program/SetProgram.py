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
print("++Intersection++")
y = {"yellow","blue","red","white"}
z= thisset.intersection(y)
print(z)

print("++Intersection Update++")
y = {"yellow","blue","red","white"}
y.intersection_update(thisset)
print(y)

print("++Symmetric Difference Update ++")
y = {"yellow","blue","red","white"}
z= thisset.symmetric_difference_update(y)
print(z)

print("++Symmetric difference++")
y = {"yellow","blue","red","white"}
z= thisset.symmetric_difference(y)
print(z)
