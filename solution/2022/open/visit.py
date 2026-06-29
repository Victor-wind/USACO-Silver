# All tests pass within 500 MS

from collections import deque

N = int(input())

graph = list()
graph.append([]) # make it 1-index
in_degree = [0] * (N+1)
visited = [0] * (N+1)
for _ in range(N):
    buddy, moos = [int (x) for x in input().split()]
    graph.append((buddy, moos))
    in_degree[buddy] += 1

dq = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        dq.append(i)

result = 0
temp_lst = []
while dq:
    k = dq.pop()
    temp_lst.append(k)
    to_visit = graph[k][0]
    result += graph[k][1]
    in_degree[to_visit] -= 1
    if in_degree[to_visit] == 0:
        dq.appendleft(to_visit)

# the remaining cows should be in 'simple' cycles, as one cow only visits one buddy
cycles = list()
for i in range(1, N+1):
    cycle = list()
    if in_degree[i] == 0 or visited[i] == 1: # already processed
        continue
    cycle.append(i) 
    visited[i] = 1   
    j = graph[i][0]    
    while visited[j] == 0:
        cycle.append(j)
        visited[j] = 1
        j = graph[j][0]
    
    cycles.append(cycle)

# process each cycle
for cycle in cycles:
    k = min(cycle, key=lambda x: graph[x][1])
    # the start point is k's next buddy graph[k][0]
    buddy_visit = graph[k][0]
    while buddy_visit != k:
        result += graph[buddy_visit][1]
        buddy_visit = graph[buddy_visit][0]
    # print(cycle, k, result)

print(result)
