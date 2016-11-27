#write a program that prints out all the elements of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist= []
for value in a:
    if value < 5:
        #print(value, " ", end=" ")
        newlist.append(value)

print(newlist)