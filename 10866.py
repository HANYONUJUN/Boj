import sys
num = int(sys.stdin.readline())
deq=[]

#1) append 함수

#arry.append(x) 형태로 사용한다. x를 arry의 맨 끝에 객체로 추가다. x가 iterable 자료형이더라도 전체를 하나의 객체로 해서 요소로 추가한다.

#2) extend 함수

#array.extend(iterable) 형태로 사용한다. iterable의 각 요소를 하나씩 array의 끝에 요소로 추가한다. append 함수와 다른 점은 괄호 안에 iterable 자료형만 올 수 있다.

#3) insert 함수

#array.insert(i, x) 형태로 사용한다. 원하는 위치 i에 x를 삽입할 수 있다. 값 x는 객체로 추가된다. append 함수와 마찬가지로 iterable 자료형이더라도 하나의 요소로 삽입된다.

 
for _ in range(num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        deq.insert(0, cmd[1])
    
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    
    elif cmd[0] == "pop_front":
        if len(deq) !=0: print(deq.pop(0))
        else : print(-1)
    
    elif cmd[0] == "pop_back":
        if len(deq) !=0: print(deq.pop())
        else : print(-1)
    
    elif cmd[0] == 'size':
        print(len(deq))
    
    elif cmd[0] == 'empty':
        if len(deq) == 0 : print(1)
        else: print(0)
    
    elif cmd[0] == 'front':
        if len(deq) == 0: print(-1)
        else: print(deq[0])
    
    elif cmd[0] == 'back':
        if len(deq) == 0: print(-1)
        else: print(deq[len(deq)-1])
     
