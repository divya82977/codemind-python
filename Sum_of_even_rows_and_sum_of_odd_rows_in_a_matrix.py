a,b=map(int,input().split())
mat=[]
se=so=0
for i in range(a):
    r=list(map(int,input().split()))
    mat.append(r)
    if i%2==0:
        se+=sum(r)
    else:
        so+=sum(r)
print(se,so)