import sys
num=int(sys.stdin.readline())
stk=[]

for _ in range(num):
    cmd=sys.stdin.readline().split()

    if cmd[0] == 'push':
        stk.insert(0, cmd[1])
    elif cmd[0] == 'pop':
        if len(stk) == 0 : print(-1)
        else : print(stk.pop(0))
    elif cmd[0] == 'size':
        print(len(stk))
    elif cmd[0] == 'empty':
        if len(stk) == 0 : print(1)
        else: print(0)
    elif cmd[0] == 'top':
        if len(stk) == 0: print(-1)
        else : print(stk[0])