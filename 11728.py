n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

arr3= a+b
arr3.sort()

answer= ' '.join(map(str,arr3))
print(answer)