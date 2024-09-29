from collections import deque

def slow_operations(target, cur):
    visit = set()
    que = deque()
    ops = 0
    que.append(cur)
    while ops < 100:
        n = len(que)
        for i in range(n):
            x = que.popleft()
            if x == target:
                return ops
            if x in visit:
                continue
            visit.add(x)
            if x >= 0:
                que.append(x+1)
                que.append(x<<1)
            if (x & 1) == 0:
                que.append(x>>1)            
        ops += 1    
    return ops

def fast_operations(from_num, to_num):
    ops = 10000000
    from_list = list()
    to_list = list()
    cur = from_num
    while cur != 1:
        from_list.append(cur)
        if (cur & 1) == 0:
            cur = cur>>1
        else:
            cur += 1
    from_list.append(1)
    ' consider from_num/to_num are binaries, the operations: >>, <<, +1 '
    ' these are fastest ways for from_num -> 1 / 1 -> to_num'
    cur = to_num
    while cur != 1:
        to_list.append(cur)
        if (cur & 1) == 0:
            cur = cur>>1
        else:
            cur -= 1
    to_list.append(1)
    #print(f'{from_list=} \n{to_list=}')        

    ''' it is possible to move to from_list[i]+1(/k), so
    (to_list[j] - from_list[i]+1(/k)) is smaller. However, that takes more ops
    The math proof can be refered in offical solution '''
    for i in range(len(from_list)):
        for j in range(len(to_list)):
            x, y = from_list[i],to_list[j]
            if y>=x:
                ops = min(ops, y-x+i+j)            
    return ops
            
N = int(input())
for _ in range(N):
    from_num, to_num = [int(x) for x in input().split()]
    print(fast_operations(from_num, to_num))
