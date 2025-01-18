# Examples of important string methods in python
#Python list methods are built-in functions that allow us to perform various operations on lists, 
# such as adding, removing, or modifying elements. 
# In this article, we’ll explore all Python list methods with a simple example.


#-----append methods in python it adds the element at the end of the list
a = [1, 2, 3, 4, 5]
a.append(5)
b = ["a", "b", "c", "d", "e", "f", "g", "h"]
b.append("5")
#---copy methods in python it does the shallow copy of the elements in the list
a = [1, 2, 3]
b = a.copy()

#----Clear method in python it removes all elements in the list
c = [1, 2, 3]
c.clear()
print (c)

#--remove methods in python it removes an element from the list---
c = [1, 2, 3]
c.remove(1)

#---count method in python it returns the number of element in list appeared
c=[1, 2, 3]

print(c.count(2))

#---Extend method in python it adds an element to the list from another list

c=[1, 2, 3]
d=[4, 5, 6]
c.extend(d)
print(c)

#---insert method in python it adds an element to the list at specified position

c=[1, 2, 3]
c.insert(1, 4)
print(c)


#---pop method from python it removes an element from the list at specified position

c=[1, 2, 3]
c.pop(1)
print(c)



#---reverse method in python it reverses the order of elements in the list
c = [1, 2, 3]

c.reverse()

print(c)