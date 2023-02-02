a=list(map(int,input().split()))

b=[ i ** 2 for i in a]
a.append(b)

print(sum(b)%10)