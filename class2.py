class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def root(self):
        print(f"the root is {self.n**0.5}")

    
n=int(input("enter a number: "))  
a=calculator(n)
a.square()
a.cube()
a.root()