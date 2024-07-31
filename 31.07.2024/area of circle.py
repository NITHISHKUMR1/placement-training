import math
def cir(n):
    return math.pi * n ** 2
n = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {radius} is {cir(n):.2f}.")
