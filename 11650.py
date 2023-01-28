import sys
input= sys.stdin.readline

num=int(input())
num_list=[]

for i in range(num):
    [a, b] = map(int,input().split())
    num_list.append([a, b])
    
s_array = sorted(num_list)

for i in range(num):
    print(s_array[i][0], s_array[i][1])



    