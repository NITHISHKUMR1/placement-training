if __name__ == '__main__':
    n = int(input().strip())  
    elements = tuple(map(int, input().strip().split()))  
    print(hash(elements)) 
