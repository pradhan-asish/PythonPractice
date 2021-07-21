myList = ["Apple","Banana","Cherry","Orange","Guava"]
print(myList)


## List is ordered, changeble, Allow duplicates


##to access list item using index

print('+++++++++++++++++')
print(myList[1])

print('+++++++++++++++++')
for i in range(len(myList)):
    print(myList[i])

print('+++++++++++++++++')
print(myList[2:5])
print(myList[:2])
print(myList[2:])
print('+++++++++++++++++')

## manipulate list item
#Insert

myList.insert(2,"Berry")
myList.append("Watermelon")
print(myList)


print('+++++++++++++++++')

## to append another list to the current list

appendList = ["Papaya","Apple","Pineapple","Pea","Pie"]
myList.extend(appendList)
print(myList)

##Remove, delete or clear elements from list

appendList.pop(1)
print(appendList)
appendList.pop()
print(appendList)
del appendList[0]
appendList.clear()
print(appendList)
del appendList
