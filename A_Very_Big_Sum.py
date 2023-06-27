n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(n):
    m.append(l[i])
print(sum(m))
