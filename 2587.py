import statistics as st
num_list=[]
for _ in range(5):
    num = int(input())
    num_list.append(num)
    num_evg=round(sum(num_list)/5)

  
print(num_evg)
print(st.median(num_list))

