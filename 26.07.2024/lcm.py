def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

n1, n2= 48, 18
print(f"The LCM of {n1} and {n2} is {lcm(n1, n2)}.")