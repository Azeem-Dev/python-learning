"""FUNCTIONS AND REGRESSIONS"""


def Sum(a,b):
    s=a+b
    return s

print(Sum(2,2),end=f" Sum of 2 + 2\n")

def calculate_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(f"factorial of number: {n} = ",fact)

calculate_factorial(5)