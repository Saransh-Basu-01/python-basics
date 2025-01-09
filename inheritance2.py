class animals:
    pass

class pets(animals):
    pass

class dogs(pets):
    @staticmethod
    def bark():
        print("bhow bhow")
    
a=dogs()
a.bark()