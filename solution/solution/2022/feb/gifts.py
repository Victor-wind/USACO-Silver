from collections import deque

N = int(input())
#print(N)
cows_prefer = []
cows_prefer.append([])
for _ in range(N):
    prefer = [ int(x) for x in input().split()]
    cows_prefer.append(prefer)

'''
with open('x.in') as f:
    lines = f.readlines()
    N = int(lines[0])
    cows_prefer = [ [int(x) for x in line.split() ] for line in lines[1:]]
    
print(N)
cows_prefer.insert(0, [])
# print(f'{cows_prefer=}')
'''

graph = list()
graph.append([])
for i in range(1,N+1):
    edges = list()
    for j in cows_prefer[i]:
        if j == i: break
        edges.append(j)
    edges.append(i)
    graph.append(edges)
        

#print(f'{graph=}')


# time complexity O(N*3): 3 tests time out
loop = [ list() for _ in range(N+1)]

def dsf_search(graph: list, src: int, dest: int, visited: set):
    #print(f'dsf_search {src} {dest}')
    if src == dest: return True
    if src in visited: # src already visited, discard it to avoid infinit loop
        return False
    visited.add(src)
    for k in graph[src]:
        if dsf_search(graph, k, dest, visited):
            return True
    return False

for i in range(1, N+1):
    # check whether j can reach i
    visited = set()
    for j in graph[i]:
        if dsf_search(graph, j, i, visited):
            loop[i].append(j)

#print(f'{loop=}')

res = [-1] * (N+1)
for i in range(1, N+1):
    for j in cows_prefer[i]:
        # if i == 2: print(f' i=2 {j=}')
        if j in loop[i]:
            res[i] = j
            break

for i in range(1, N+1):
    print(res[i])
    
'''

#  Floyd-Warshall : it has worse performance only 3 tests pass
reachable = [ [0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):  
    for j in graph[i]:        
        reachable[i][j] = 1    

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if reachable[i][k] == 1 and reachable[k][j] == 1:
                reachable[i][j] = 1
            
for i in range(1, N+1):
    for j in cows_prefer[i]:
        if reachable[j][i] == 1:
            print(j)
            break
    
'''


