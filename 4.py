"""
LOOPS
"""
i=0
while i < 5:
    print(f'Hello World # {i+1}')
    i+=1
    
vals = [1,2,3,4,5]

for val in vals:
    print(val)
else: 
    # anything that we want to perform after complete loop
    # executes we place it in else statement. But if the loop
    # breaks in between then else doesn't runs
    print("RUNS AFTER LOOP ENDS. THIS IS OPTIONAL")
    

for el in range(10): #returns a seqence of numbers and incr-
                    #ement by 1 by default
    print(el)
print("\n\n\n")
    
for el in range(1,10):#returns a seqence of numbers starting from 1 index
                    #and increment by 1 by default
    print(el)
print("\n\n\n")

for el in range(1,10,2):#returns a seqence of numbers starting from 1 index
                    #and increment by 2.
    print(el)
print("\n\n\n")


for el in range(10,2,-2):#returns a seqence of numbers starting from 1 index
                    #and increment by 2.
    print(el)