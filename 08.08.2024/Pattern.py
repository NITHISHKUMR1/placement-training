def num(u):
    n = 1
    for i in range(0, u):
        n = 1
        for j in range(0, i+1):
            print(n, end=" ")
            n = n + 1
        print("\r")
u=int(input("Enter the range: "))
num(u)
