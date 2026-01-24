# All tests pass within 400 ms 

import sys
from collections import deque

N = int(sys.stdin.readline())
roads = [ [int(x) for x in sys.stdin.readline().split()] for _ in range(N-1)]
#print(roads)
grid = [ [] for i in range(N+1)]
for farm_a, farm_b in roads:
    # print(farm_a, farm_b)
    grid[farm_a].append(farm_b)
    grid[farm_b].append(farm_a)
# start from farm 1, bfs all farms
visited = [0] * (N+1)
to_visit = deque()
to_visit.append(1)
result = 0


def add_days(farm): # how many days an infected cow needs to stay at farm 
    #print(f'visit {farm=}')
    k = 0 # how many infected cows needed: self + next farms
    for nxt in grid[farm]:
        if not visited[nxt]:
            k += 1
    if k == 0: # don't need to send infected cows to neighbor farms 
        return 0
    
    res = 0
    k += 1 # add itself
    x = 1
    # to get k sicked cows
    while x < k:
        x = x << 1
        res += 1       
    #print(f'visit {res=} {(k-1)=}')
    # add days to send cows to neighbor farms
    return res + (k-1)

while to_visit:
    farm = to_visit.popleft()
    if visited[farm]: continue
    result += add_days(farm)
    visited[farm] = True
    for nxt in grid[farm]:
        if visited[nxt]:
            continue
        to_visit.append(nxt)

print(result)        
    
