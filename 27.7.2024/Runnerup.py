if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sco=list(set(arr))
    sot=sorted(sco,reverse=True)
    print(sot[1])
