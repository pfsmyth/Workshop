# Lists

#create an empty list
myList = []

#create list with values
myList2 = [ 5,8,9]

# Items in the list don't all have to be the same type
myList3 = ['Hello', 42, 3.142 ]

# individual elements in the list can be referenced
print myList3[0]

# to iterate over all of the elements in a list
for x in myList3 :
    print x

#to add an element
myList3.append("new item")

# how many items in the list
print len(myList3)

# print last element remembering that the indexing starts at 0
print myList3[len(myList3) - 1]

# or more simply (counting backwards from the end)
print myList3[-1]

#to delete an item
del myList3[2]

for x in myList3 :
    print x


