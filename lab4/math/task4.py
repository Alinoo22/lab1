def count_squared_up_to(a , b): 
    while a <= b:
        yield a*a
        a += 1
a = int(input("a:"))
b = int(input("b:"))
for number in count_squared_up_to(a , b):
    print(number)