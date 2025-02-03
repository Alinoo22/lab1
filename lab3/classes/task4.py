import math
class Points:
    def __init__(self, x, y):       
        self.x = x
        self.y = y

    def show(self):
        print("Current X coordinate:", self.x)
        print("Current Y coordinate:", self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def dist(self, coords2):
        dis = math.sqrt((pow((self.x - coords2.x), 2) + pow((self.y - coords2.y), 2)))
        return dis

x1 = int(input("enter X coordinate: "))
y1 = int(input("enter Y coordinate: "))
coords1 = Points(x1, y1)

coords1.show()
command = input("enter command distance: ")
if command == "move":
    newX = input("enter new x coordinate: ")
    newY = input("enter new y coordinate: ")
    coords1.move(newX, newY)
    coords1.show()
elif command == "distance":
    newX = int(input("enter the second point's x coordinate: "))
    newY = int(input("enter the second point's y coordinate: "))
    coords2 = Points(newX, newY)
    print("distance between them:", coords1.dist(coords2))