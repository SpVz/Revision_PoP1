a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

a=set(a)
b=set(b)

c=a & b
c=list(c)
print(c)
