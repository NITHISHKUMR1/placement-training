n=int(input('Enter value of n: '))
p=int(input('Enter value of p: '))

temp=n
n=p
p=temp

print('The value of x after swapping: {}'.format(n))
print('The value of y after swapping: {}'.format(p))