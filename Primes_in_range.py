def is_prime(n):
    if n<2:
        return False
    import math
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
n=int(input())
b=int(input())
c=0
for i in range(n,b+1):
    if is_prime(i)==True:
        c+=1
    else:
        c==0
print(c)
    