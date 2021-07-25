###########Dictonary#############

thisDict = {"brand" : "BMW",
            "model" : "Q3",
            "year" : 2001}



#########Dictionary are ordered after 3.7 version python prior to that it was unordered#########
#########Dictionary are Changeable
########Duplicates are not allowed
print(thisDict)
print('++++++How to access dictionary++++++')
print(thisDict["brand"])
print('++++++How to access dictionary++++++')
x= thisDict.keys()
print('++++++Dictionary keys++++++')
print(x)

y = thisDict.values()
print('++++++Dictionary values++++++')
print(y)

thisDict["color"]  =  "red"
print(thisDict)

print('++++++Values using get statement++++++')
x = thisDict.get("model")
print(x)

print('++++++year updationt++++++')
thisDict.update({"year": 2010})
print(thisDict)

#####Loop
for x in thisDict:
    print(x)

print('++++++items access++++++')
for x,y in thisDict.items():
    print(x,y)



##Copy dictionaries
print('++++++items copied++++++')
copyDict = thisDict.copy()
print(copyDict)

##Nested dictionaries

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print('++++++Nested dictionaries++++++')

print(myfamily)


