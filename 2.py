"""
TUPLES AND LISTS
"""

"""
LISTS
"""
marks = [14.4, 10.5, 10.6, 13.4, 14.5] #list

print(marks)
print(len(marks))

print(marks[0])
print(marks[1])
print(marks[2])

marks[0]=14.7
print(marks)

randomList = ["data","number",85,8.5,-16]
print(randomList)

"""LIST SLICING IS SIMILAR TO STRING SLICING"""

marks.append(10) #adds one element at the end
marks.sort() #sorts in ascending order
marks.sort(reverse=True) #sorts in descending order
marks.reverse() #reverses the list
idx=1
el=15.5
marks.insert(idx,el) #inserts at specified index
marks.remove(10) #removes first occurence of passed element
marks.pop(idx) #removes element at index 
copiedList = marks.copy() #makes a shallow copy of the list
print(f"copied list {copiedList}")




"""
TUPLES
"""

#CREATES IMMUTABLE SEQUENCE OF VALUES

tup=(10,12,14,16,18)
print(tup[0])
print(tup[1])
print(tup[2])

tup2 = ()
print(tup2)
print(type(tup2))

#if we have a single value tuple then always place a comma
tup3 = (1,)
print(tup3)

print(tup[:3])

print(tup.index(12))
print(tup.count(12))