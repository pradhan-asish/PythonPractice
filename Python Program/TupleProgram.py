################Tuples###############
##Ordered, Unchangeable, Allow Duplicates##
myTuple = ("apple","banana","guava","banana","apple")
print(myTuple)


## Tuples
print('+++Using Indexes+++')
print(myTuple[1])
print(myTuple[1:3])
print(myTuple[-2])

## update Tuples
print('+++Add of new element+++')
y= list(myTuple)
y.append("kiwi")
myTuple = tuple(y)
print(myTuple)

z = list(myTuple)
z.remove("banana")
myTuple= tuple(z)
print(myTuple)

##Joins and Multiply Tuple
print('+++Joins and Multiply+++')
l = ("red","berry")
k = myTuple + l
print(k)
print('+++Multiply by 2+++')
print(k*2)

##Tuple Counts and index

print(myTuple.count("apple"))
print(myTuple.index("banana"))



