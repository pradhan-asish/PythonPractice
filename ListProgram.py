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
print('+++++++++++++++++')

##Remove, delete or clear elements from list

appendList.pop(1)
print(appendList)
appendList.pop()
print(appendList)
del appendList[0]
appendList.clear()
print(appendList)
del appendList
print('+++++++++++++++++')


##loop
print('++++++ For+++++++++++')
for x in myList:
    print(x)

print('++++++While+++++++++++')
i= 0
while i < len(myList):
    print(myList[i])
    i=i+1
print('++++++One Line+++++++++++')
[print(z) for z in myList]
