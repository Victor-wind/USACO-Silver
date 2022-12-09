import sys
sys.setrecursionlimit(100000)

with open('fenceplan.in') as f:
    lines = f.readlines()

N, M = [int(x) for x in lines[0].split()]
print(N, M)

cows = [ [ int(v) for v in line.split()] for line in lines[1:N+1]]
#print(f'{cows}')

moos =  [ [ int(v) for v in line.split()] for line in lines[N+1:]]
#print(f'{moos}')
res = 0            

edges = dict()
for c in moos:
    c1, c2 = c
    edges.setdefault(c1, []).append(c2)
    edges.setdefault(c2, []).append(c1)

#print(f'{edges}')   
cows_groups = list()

def dfs_search(edges: dict, visited: list, group: list, node: int):
    if visited[node] == 1:
        return
    group.append(node)
    visited[node] = 1
    for i in edges[node]:
        dfs_search(edges, visited, group, i)

        
def group_cows(edges: dict, cows_groups: list):
    visited = [0] * (N+1)
    for k, v in edges.items():
        group = list()
        if  visited[k] == 1:
            continue # alreay in other groups
        dfs_search(edges, visited, group, k)
        cows_groups.append(group)        
        
group_cows(edges, cows_groups)   

#print(cows_groups)

res = 40000000000
for group in cows_groups:
    x_min, x_max = 10000000000, 0
    y_min, y_max = 10000000000, 0
    for i in group:
        x_min = min(x_min, cows[i-1][0])
        x_max = max(x_max, cows[i-1][0])
        y_min = min(y_min, cows[i-1][1])
        y_max = max(y_max, cows[i-1][1])
    fence = (x_max-x_min)*2+(y_max-y_min)*2
    res = min(res, fence)

print(res)
with open('fenceplan.out', 'a') as f:
    f.write(f'{res}'+'\n')       
