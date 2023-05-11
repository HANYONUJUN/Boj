num=int(input())
word_list=list(input())

a,b=0,0

for i in range(num):
    if word_list[i] =='A':
        a+=1
    else:
        b+=1


if a>b:
    print('A')
elif a == b:
    print('Tie')
else:
    print('B')

    