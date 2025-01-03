"""DICTIONARIES AND SET"""
dict={
    "name":"Rafay",
    "cgpa":3.97,
    "marks":[10,11,12,13,14]
}
print(dict["name"],dict["cgpa"],dict["marks"])
dict["yearOfGrad"]="2024"
print(dict)

"""
WE CAN ALSO CREATE NESTED DICTIONARY LIKE BELOW

"""

#EXAMPLE
nested_dict = {
    "name":"Rafay",
    "cgpa":3.97,
    "marks":[10,11,12,13,14],
    "grades": {
        "a":90,
        "b":80,
        "c":70
    }
}
print(nested_dict)
print(nested_dict["grades"]["a"])


"""
METHODS
"""

print(nested_dict.keys()) #returns all keys
print(nested_dict.values()) #returns all values
print(nested_dict.items()) #returns all (key,val) pairs as tuples
print(nested_dict.get("name")) #returns the key according to value

nested_dict.update(
    {
    "test_key":"some value"
    }
    ) #inserts specified values to the dictionary
print(
    nested_dict
      ) 

pairs=list(nested_dict.items())
print(pairs)



"""
SET (IS A UNIQUE IMMUTABLE ELEMENTS) SO IT DOESN"T ACCEPTS LIST AND DICTIONARY ONLY OTHER VALUES

"""

nums = {1,2,3,4}
nums1 = {1,2,3,4,3,4,1,2,1}
print("nums",nums)
print("nums1",nums1)

null_set=set()

el="Test"

null_set = null_set.union(nums1)
print(null_set)

null_set.add(el) #adds a value to the set
print(null_set)

null_set.remove(el) #removes given element
print(null_set)

null_set.pop() # removes a random value
print(null_set)

null_set = null_set.union({6,7}) # removes a random value
print(null_set)

null_set = null_set.intersection({1,2,6,7}) # removes a random value
print(null_set)

null_set.clear() # clean the set
print(null_set)