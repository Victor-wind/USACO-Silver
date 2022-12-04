from collections import deque
# time out for case 8, 10
'''
with open('closing.in') as f:
    lines = f.readlines()

N, M = [int(x) for x in lines[0].split()]
print(N,M)

connected = [ [int(i) for i in x.split()] for x in lines[1:1+M]]
#print(f'{connected=}')

edges = { i: [] for i in range(1, N+1) } 
for c in connected:
    c1, c2 = c[0], c[1]   
    edges[c1].append(c2)
    edges[c2].append(c1)

#print(f'{edges=}')

barns = [int(x) for x in lines[1+M:]]
#print(f'{barns=}')
'''

with open('closing.in', 'r') as r:
    N, M = [ int(x) for x in r.readline().split()]
    print(N,M)
    edges = { i: [] for i in range(1, N+1) } 
    for _ in range(M):
        c1, c2 = tuple(map(int, r.readline().split()))
        edges[c1].append(c2)
        edges[c2].append(c1)
    #print(f'{edges=}')
    
    barns = [ int(r.readline()) for _ in range(N)]
    #print(f'{barns=}')

res = []

nodes = [1 for i in range(0, N+1)]
nodes[0] = None
# print(f'{nodes}')

def check_connected(nodes: list, edges: dict) -> str:
    # find the first valid node to start BFS
    for i in range(N+1):
        if nodes[i] != None: break
    if i == N : return 'YES' # all nodes disconnected
    q = deque()
    q.append(i)
    nodes[i] = 0    
    while len(q):
        x = q.popleft()
        for k in edges[x]:
            if nodes[k] == 1:
                q.append(k)
                nodes[k] = 0

    res = 'YES'
    for i in range(N+1):
        if nodes[i] == 1: res = 'NO'
        if nodes[i] != None: nodes[i] = 1 # restore nodes status

    return res


res.append(check_connected(nodes, edges))

for barn in barns:
    nodes[barn] = None
    # print(f'in loop {barn=} {nodes=} {res=}')
    res.append(check_connected(nodes, edges))
    # print(f'after loop {res=}')

# remove last one
res.pop()
# print(res)

with open('closing.out','w') as f:
    for x in res:
        f.write(f'{x}\n')
'''
with open('closing.out','w') as f:
    connected = check_connected(nodes, edges)
    f.write(f'{connected}\n')
    for i in range(N-1):
        barn = barns[i]
        nodes[barn] = None
        connected = check_connected(nodes, edges)
        f.write(f'{connected}\n')
'''        
    


