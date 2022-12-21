from collections import deque
import sys

#sys.setrecursionlimit(100000)


test_cases = list()


T = int(input())

for i in range(T):
    N, M = [int(x) for x in input().split()]
    graph = dict()
    for j in range(M):
        u, v = [int(x) for x in input().split()]
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    #print(f'{N} {M}')
    #print(f'{graph=}')
    case = { 'N': N, 'M': M, 'graph': graph}
    test_cases.append(case)

#print(test_cases)
'''
with open('x.in') as f:    
    T = int(f.readline())
    print(T)
    for i in range(T):
        N, M = [int(x) for x in f.readline().split()]
        print(N,M)
        graph = dict()
        for j in range(M):
            u, v = [int(x) for x in f.readline().split()]
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        #print(f'{graph=}')
        case = { 'N': N, 'M': M, 'graph': graph}
        test_cases.append(case)

'''

def cost_between_groups(group1: list, group2: list):
    n1 = len(group1)
    n2 = len(group2)
    i,j = 0, 0
    min_cost = (group1[0]-group2[0])**2
    
    while i < n1 and j < n2:
        while i<n1 and j<n2 and group1[i] <= group2[j]:
            min_cost = min(min_cost, (group1[i]-group2[j])**2 )
            i+=1
        while j<n2 and i<n1 and group2[j] <= group1[i]:
            min_cost = min(min_cost, (group1[i]-group2[j])**2 )
            j+=1
        
    return min_cost


def get_cost2(N:int, groups: list):
    # barn 1 must be in group[0], but barn n may not in group[-1]
    for g in groups:
        if g[-1] == N:
            dst_group = g

    # the cost of building one path
    min_cost = cost_between_groups(groups[0], dst_group)

    # the cost of buiding two paths
    for g in groups[1:]:
        cost1 = cost_between_groups(groups[0], g)
        cost2 = cost_between_groups(dst_group, g)
        min_cost = min(min_cost, cost1+cost2)
        #print(f'in loop {g=}')
    
    return min_cost


def dist_to_group(group: list, costs: list, N: int):
    M = len(group)
    i,j = 0,1
    # using two pointers to find the cost to the group for all nodes from 1 to N 
    while i < M and j < N+1:
        while i < M and group[i] <= j:
            i+=1
        i-=1
        # now group[i] <= j and group[i+1] > j
        # for node j, the cost to the group is min(cost to group[i], cost to group[i+1])
        dist_1 = j - group[i] if i >=0 else 100000
        dist_2 = group[i+1]-j if i+1 < M else 100000
        costs[j] = min(dist_1,dist_2) **2
        j += 1
        if i < 0:
            i = 0  
    

def get_cost(N:int, groups: list):
    # barn 1 must be in group[0], but barn n may not in group[-1]
   for g in groups:
        if g[-1] == N:
            dst_group = g
   src_group =  groups[0]

   # dist_src stores the costs of all nodes to src_group
   dist_src = [10000000000] * (N+1)
   # dist_dst stores the costs of all nodes to dst_group
   dist_dst = [10000000000] * (N+1)

   dist_to_group(src_group, dist_src, N)
   dist_to_group(dst_group, dist_dst, N)

   min_cost = 10000000000
   # the cost of building one path from src_group to dst_group
   for i in dst_group:
       min_cost = min(min_cost, dist_src[i])
   
   # the cost of buiding two paths through the third group
   for g in groups:
       if g == src_group or g == dst_group:
           continue
       cost_src, cost_dst = 10000000000, 10000000000
       for i in g:
           cost_src = min(cost_src, dist_src[i])
           cost_dst = min(cost_dst, dist_dst[i])
       min_cost = min(min_cost, cost_src+cost_dst) 
           
   return min_cost

# For test cases 6 -10. DFS causes maximum recursion depth exceeded in comparison
def dfs_search(node: int, visited:list, group: list, graph:dict):
    if visited[node] == 1: # already in other group
        return
    visited[node] = 1
    group.append(node)

    for i in graph[node]:
        dfs_search(i, visited, group, graph)
    
def bfs_search(node: int, visited:list, group: list, graph:dict):
    if visited[node] == 1: # already in other group
        return    
    q = deque()
    q.append(node)
    group.append(node)
    visited[node] = 1
    while len(q) > 0:
        i =q.popleft()
        for k in graph[i]:
            if visited[k] == 0:
                q.append(k)
                group.append(k)
                visited[k] = 1
    return group            
        

def group_barns(N, M, graph: dict):
    groups = list()
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i] == 1: # already in other group
            continue
        if i not in graph: # not in graph, it is a seperate node 
            groups.append([i])
            continue
        group = list()
        # dfs_search(i, visited, group, graph)
        bfs_search(i, visited, group, graph)
        group.sort()
        groups.append(group)
    # barn 1 must be in group[0], but barn n may not in group[-1]
    return groups    
    

for case in test_cases:
    N = case['N']
    M = case['M']
    graph = case['graph']
    groups = group_barns(N, M, graph)
    #Test case 7 ~10 will time out
    cost = get_cost(N, groups)
    print(cost)
    
