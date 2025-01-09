class vector2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is {self.i}i+{self.j}j")


class vector3d(vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k 

    def show(self):
        print(f"the vector is {self.i}i+{self.j}j+{self.k}k")

a=vector2d(1,2)
a.show()
b=vector3d(2,4,3)
b.show()