coin=100
n,m=map(int,input().split())
n=n*coin
if(n >= m):
    print("Yes")
else:
    print("No")