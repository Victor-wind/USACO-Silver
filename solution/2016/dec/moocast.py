from collections import deque

with open('moocast.in') as f:
    lines = f.readlines()

N = int(lines[0])
print(N)

cows = [ [int(i) for i in x.split()] for x in lines[1:]]
# print(cows)

edges = [ [] for i in range(N)]
for i in range(N):
    cow_i_x, cow_i_y, cow_i_p = cows[i]
    for j in range(i+1, N):
        cow_j_x, cow_j_y, cow_j_p = cows[j]
        dist = (cow_i_x-cow_j_x)* (cow_i_x-cow_j_x) + (cow_i_y-cow_j_y)*(cow_i_y-cow_j_y)
        if cow_i_p * cow_i_p >= dist:
            edges[i].append(j)
        if cow_j_p * cow_j_p >= dist:
            edges[j].append(i)
# print(edges)   
res = 0

def check_connect(edges: list, k: int )-> int:
    visited = [0] * N
    q = deque()
    q.append(k)
    visited[k] = 1
    res = 1
    while len(q):
        x = q.popleft()
        for y in edges[x]:
            if visited[y] == 0:
                visited[y] = 1
                res += 1
                q.append(y)
    return res

for i in range(N):
    res = max(res, check_connect(edges, i))

print(res)
with open('moocast.out','w') as f:
    f.write(f'{res}\n')
