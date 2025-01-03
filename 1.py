
#NEW APPLICATION
name = 'Azeem'
age = 29
price = 25.99
isNewPrice=True

"""
BELOW IS THE PRINTING AND TYPE PRINTING OF THESE
TYPES.
"""

print('VALUES',name,age,price,isNewPrice)
print('TYPES',type(name),type(age),type(price),type(isNewPrice))


"""
WE ARE NOW LOOKING INTO OPERATORS
"""
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulus/remainder
print(a**b) #Power

"""
WE ARE NOW LOOKING INTO LOGICAL OPERATORS
"""
print(not False) #here not == !
print(not True) #here not == !

"""
TYPE CONVERSION AND CASTING
"""

#TYPE CONVERSION

a=3.14
b=10
sum=a+b
print('Type Conversion',sum)



#TYPE CASTING

c="2.5"
d=10
newSum = float(c) + d
print('Type casting',newSum)

e="2"
f=10
neSum = int(2) + d
print('Type casting',neSum)



"""
INPUT
"""
username=input("Enter your name:")
print("Welcome",username)


"""
STRINGS
"""
str = "DevsCorp"
print(len(str))
print(f'{str[0]} {str[1]} {str[2]} {str[3]}')

"""
STRING SLICING
"""
# str[starting_index,ending_index] ending_index is not included

print(str[1:3])
print(str[:3]) # this is similar to str[0:3]
print(str[1:]) # this is similar to str[1:len(str)]


"""
STRING NEGATIVE INDEX
"""

newStr = "Apple" #  A   p   p   l   e
                #  -5  -4  -3  -2  -1 
                
print(newStr[-4:-1]) #negative slicing

print("endsWith Method:",newStr.endswith(".")) # return true or false
print("capitalize Method:",newStr.capitalize()) # capitalize first charachter
print("count Method:",newStr.count("p")) # counts the instance of passed value i.e. "P" or some substring
print("find Method:",newStr.find("p")) # finds the first instance of charachter passed
print("replace Method:",newStr.replace("p","1")) # replaces characters with new value i.e old, new
print("String that was created originally:",newStr)



"""
Conditional Statements
"""

#if-elif-else

age = int(input("Please enter ur age:"))
if(age >= 18 and age < 61):
    print("You can create a CNIC for 10 years max")
elif(age>=61):
    print("You can create a CNIC for lifetime")
else:
    print("You can't create a CNIC yet.")
