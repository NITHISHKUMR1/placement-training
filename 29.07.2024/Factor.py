def f(n):
    fac = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            fac.append(i)
            if i != n // i:
                fac.append(n // i)
    fac.sort()
    return fac
num= int(input("Enter a number to find its factors: "))
fac = find_factors(num)
print(f"The factors of {num} are: {fac}")
