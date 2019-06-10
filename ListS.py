thisList = ["Platanos", "Manzana", "Peras", "etc"]
print(thisList)

# Access item
print(thisList[0])

# Change valu
thisList[1] = "Uva";
print(thisList)

# Loop Trought a list
thisList = ["Maria", "Juan", "Karla", "Andrea", "Joselyn"]
for x in thisList:
    print(x)

# Check if item exists
thisList = ["Lauisa", "Juana", "Josely"]
if "Juana" in thisList:
    print("Yes, 'Juana' is in the names list")


#List leght


thisList = [1,1,2,12,2,12,12,12,1,2,12,1,2,12,1,21,2,12]
print(len(thisList))

#Add items

thisList = ["Orange","Banana","Cherry"]
thisList.append("Apple")
print(thisList)
thisList.insert(1,"Other")
print(thisList)

#Remove itemse

thisList = ["Orange","Banana","Cherry"]
thisList.remove("Orange")
print(thisList)

print("-------------------------------")
thislist = ["apple", "banana", "cherry"]
thisList.pop()

print(thisList)


print('--------------------------')
thislist = ["apple", "banana", "cherry"]
#thisList.clear()
print(thisList)

thislist = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)


thislist = ["apple", "banana", "cherry"]
myList = list(thisList)
print(myList)


#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)