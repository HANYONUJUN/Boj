import math

def lcm(a,b):
    result =(a*b) // math.gcd(a,b)
    return result

n = int(input())

for _ in range(n):
    m,n=map(int,input().split())

    print(lcm(m,n))

