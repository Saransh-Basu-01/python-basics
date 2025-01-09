class complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    def __add__(self, c2):
        # Add the real parts and imaginary parts
        #return complex(self.r + c2.r, self.i + c2.i)
        real_part=self.r+c2.r
        img_part=self.i+c2.i
        return complex(real_part,img_part)

    def __mul__(self, c2):
        # Multiply two complex numbers: (a+bi) * (c+di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        imaginary_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imaginary_part)

    def __str__(self):
        # Return a readable string for the complex number in "a + bi" format
        return f"{self.r} + {self.i}i"

    def show(self):
        # Print the complex number
        print(f"{self.r} + {self.i}i")


# Creating complex numbers
c1 = complex(1, 2)
c2 = complex(2, 3)

# Displaying the complex numbers
c1.show()  # Output: 1 + 2i
c2.show()  # Output: 2 + 3i

# Adding two complex numbers
print("Sum:", c1 + c2)  # Output: Sum: 3 + 5i

# Multiplying two complex numbers
print("Product:", c1 * c2)  # Output: Product: -4 + 7i
