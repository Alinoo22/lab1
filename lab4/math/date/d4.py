from datetime import datetime
a = datetime.now()
b = datetime(2007, 8, 3)
difference = a - b  
seconds = difference.total_seconds()
print(seconds)