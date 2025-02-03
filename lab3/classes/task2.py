
class Shape:
    def __init__(self):  
        self.area = 0  

    def find_area(self):
        return self.area  

class Square(Shape):
    def __init__(self, length):  
        super().__init__()  
        self.length = length  

    def find_area(self):
        self.area = self.length * self.length  
        return self.area  


a = int(input("Enter length: "))  
sqr = Square(a)  

print("Default area:", sqr.area) 
print("Calculated area:", sqr.find_area()) 