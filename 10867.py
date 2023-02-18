num=int(input())
num_list=list(map(int,input().split()))

num_list=list(set(num_list))
num_list.sort()

answer=' '.join(map(str,num_list))

print(answer)




