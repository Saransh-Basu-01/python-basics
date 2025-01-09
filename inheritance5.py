class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,v2):
        i=self.i+v2.i
        j=self.j+v2.j
        k=self.k+v2.k
        return vector(i,j,k)
    def __mul__(self,v2):
        result=vector(self.i*v2.i,self.j*v2.j,self.k*v2.k)
        return result
    def show(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    
v1=vector(1,2,3)
v2=vector(2,3,1)
# print(v1) 
# print(v2)
v1.show()
v2.show()
v3=v1+v2
v3.show()
print(v1*v2)