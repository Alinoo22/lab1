import math

num = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

area = (num * a * a)/(4 * math.tan(math.pi / num))
print("The area of the polygon is:", area)