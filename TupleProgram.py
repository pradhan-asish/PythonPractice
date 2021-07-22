################Tuples###############
##Ordered, Unchangeable, Allow Duplicates##
myTuple = ("apple","banana","guava","orange","papaya")
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



