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

class Rectangle(Shape):
    def __init__(self, length, width):  
        super().__init__()  
        self.length = length  
        self.width = width  

    def find_area(self):
        self.area = self.length * self.width  
        return self.area
    
# Let's check it
a = int(input("Enter length of square: "))  
sqr = Square(a)  
b = int(input("Enter length of rectangle: "))
c = int(input("Enter width of rectangle: "))
rect = Rectangle(b, c)

print("Square area:", sqr.find_area())  
print("Rectangle area:", rect.find_area()) 