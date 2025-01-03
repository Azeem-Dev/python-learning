"""
IN THIS FILE WE ARE GOING TO CREATE A CLASS WHICH WILL CREATE COMPLEX NUMBERS

x.i + y.j in here x and y can be replaced by any number the part with i is called real and part with j is called imaginary e.g.

1i + 3j

here 1i is real and 3j is imaginary

when adding two complex numbers i.e.

  1i + 3j
+ 2i + 5j
----------
  3i + 8j

Here real part and complex part is added seperately means:

1i+2i and 3j+5j


SO LET'S START
"""


class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} i + {self.img} j")

# the below method is called dunder method which replaces + for this class
    def __add__(self, num: 'ComplexNumber') -> 'ComplexNumber':
        newReal = self.real + num.real
        newImg = self.img + num.img
        return ComplexNumber(newReal, newImg)


num1 = ComplexNumber(1, 5)
num2 = ComplexNumber(4, 6)
num1.showNumber()
num2.showNumber()
# below using dunder method
num3 = num1 + num2
num3.showNumber()
