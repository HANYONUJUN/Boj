from copy import copy
n=int(input())

for _ in range(n):
    num=int(input())
    num2 = copy(num)
    print(num , num2)
