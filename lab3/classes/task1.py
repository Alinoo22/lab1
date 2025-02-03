class siclass:
     def __init__(self):
        self.text = ""
     def getString(self):
        self.text = input()
    
     def printString(self):
        print(self.text.upper())


obj = siclass()
obj.getString()
obj.printString()

