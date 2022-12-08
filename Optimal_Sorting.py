n=int(input())
for i in range(n):
    a=int(input())
    lst=list(map(int,input().split()))
    if(lst==sorted(lst)):
        print("0")
    else:
        print(max(lst)-min(lst))