import math
import time
num = int(input("Введите число: "))
milli = int(input("Введите какое-то число в миллисекундах: "))
print("Думает... хмммм... 🤔")
time.sleep(milli/1000)
num_sqrt = math.sqrt(num)
print(f'Square root of {num} after {milli} miliseconds is {num_sqrt}')