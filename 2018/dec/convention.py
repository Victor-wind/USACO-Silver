
with open('convention.in') as f:
    lines = f.readlines()

N, M, C = [int(x) for x in lines[0].split()]
print(N, M, C)

arrive_t = [int(x) for x in lines[1].split() ]
arrive_t.sort()
#print(arrive_t)

def can_move_all_cows(wait: int, arrive_t: list, M: int, C: int) -> bool:
    bus = 1
    cnt = 0
    start_t = arrive_t[0]
    for t in arrive_t:
        cnt +=1
        if (t - start_t) > wait or cnt > C:
            bus += 1
            cnt = 1
            start_t = t
    return bus <= M
    

min_wait_t = arrive_t[-1]

left  = 0
right = min_wait_t

# For given max wait time t1, check whether it can move all cows with M buses
# if t1 = arrive_t[-1], it definitely can; if t1 = 0, it can not
# We also know that if t1 can, then for any t2 > t1, t2 also can.
# If we draw a graph with x-axis as max wait time, and y-axis as Yes/No.
# the graph will be N N, ... , N, N, Y, Y, ..., Y.
# We need to find the smallest time on the graph, at which the y is Yes.

while left < right:
    mid = (left+right)//2
    if can_move_all_cows(mid, arrive_t, M, C):
        right = mid
    else:
        left = mid+1
        
print(left)
with open('convention.out','w') as f:
    f.write(f'{left}\n')
 
