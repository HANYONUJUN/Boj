n=int(input())
word_list=[]

for _ in range(n):
    word=input()
    word_list.append(word)

word_un = list(set(word_list))
word_un.sort(key=lambda x : (len(x), x.lower()))

for i in word_un:
    print(i)