#Lists in python
   #A built in data type that stores set of values..
   #it can store elements of different types(integer,float,string,etc..)
""" 
marks1=20.5
marks2=22.5
marks3=30.5
marks4=40
print(marks1,marks2,marks3)
"""
#indexing happen in List

#Create a list of five fruit and print it

fruits=["Mango", "Banana","Apple","Orange","papaya"]
"""
print(fruits)

#Access Elements From a list
   #First and last element of a list

print(fruits[0])   #First element
print(fruits[-1])  #last element

#Modify an element in a list
    #change banana to pineapple in the list
fruits[1]="pineapple"
print(fruits)

#Add an element to a list
    #Append grapes to list
fruits.append("Grapes")
print(fruits)

#Insert an Element at a specific position
   #insert "milk" At index 3 in the list
   
fruits.insert(3, "Milk")
print(fruits)

#remove an element from a list
    #remove grapes from list
fruits.remove("Grapes")
print(fruits)
  #remove at specific position(remove milk at index 3)

 #fruits.remove(3, "Milk")  (wrong syntax)
#print(fruits)

#pop an element from a list(remove last element using pop() method)
fruits.pop() #remove last element
print(fruits)

#Loop through a list(print element of the list usung a loop)

for fruit in fruits:
    print(fruit)

for Apple in fruits:
    print(fruits)

#check if an item is present
if "Bottle" in fruits:
    print("Cbottle is in the list")

if "Mango" in fruits:
    print("Mango is in list")
    
if "papaya" in fruits:
    print("Papaya")
"""
#Sort a list
fruits.sort
print(fruits)
#reverse a list
reversed_list= fruits[:: -1]
print(reversed_list)
