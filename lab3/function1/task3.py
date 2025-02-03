def solve(numheads, numlegs):
    rabbit = int((numlegs - (numheads * 2))/2)
    chicken = int(numheads - rabbit)
    print("It's", rabbit, "rabbits", "and", chicken, "chickens")

heads = int(input("Heads: "))
legs = int(input("Legs: "))
solve(heads, legs)