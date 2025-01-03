import os # OS is a module

"""FILE INPUT OUTPUT"""
file = open("sample.txt","rt")
data = file.read()
file.close()
print(data)
print(type(data))

file = open("sample.txt","rt")
data = file.read(3) #reads only the first n number of charachters defined
file.close()
print(data)
print(type(data))


file = open("sample.txt","a+")
file.write('\nThis is a new line added programatically 123')
file.seek(0)  # Reset the file pointer to the beginning
line1 = file.readline().replace('\n','') #reads line
line2 = file.readline().replace('\n','') #reads line
line3 = file.readline().replace('\n','') #reads line
file.close()
print("READING STARTED\n",f'{line1}\n',f'{line2}\n',line3)


with open("sample.txt","rt") as openedFile: #word after as is called alias and using as is called aliasing
    print(openedFile.read())
    openedFile.close()

# os.remove("sample.txt")