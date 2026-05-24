# Test case 7 times out, other tests cases pass within 1500 ms

import sys
from collections import deque

N, M = [int(x) for x in sys.stdin.readline().split()]
graph = [ list() for _ in range(M+1)]
cows = [(-1,-1)]
# the graph could have parallel edges between vertex, A<->B
# to detect the cycle, each edge has an ID, which is the cow id
for i in range(N):
    f,s = [int(x) for x in sys.stdin.readline().split()]
    cows.append((f,s))
    graph[f].append((s, i+1)) # (s, and edge_id/cow_id)
    graph[s].append((f, i+1)) # (f, and edge_id/cow_id)

def bfs_find_cycle(i):
    local_visited = [0] * (M+1)
    if i in local_visited: return None
    que = deque()
    que.append((i, -1))
    local_visited[i] = 1
    while que:
        v, p_edge = que.popleft()
        for n, e_id in graph[v]: # e_id is the cow id
            if e_id == p_edge:
                continue
            if local_visited[n]:
                return e_id
            local_visited[n] = 1
            que.append((n,e_id))
    return None

cow_orders = list()
def bfs_find_permutation(i):
    que = deque()
    # the parent edge is not necessary, as doesn't need to detect cycle
    que.append(i)
    visited[i] = 1
    while que:
        v = que.popleft()
        for n, e_id in graph[v]: # e_id is the cow id
            if e_id in removed_edge: # edge is removed to break the cycle
                continue
            if visited[n]:
                continue
            visited[n] = 1
            que.append(n)
            # cereal (n) is assigned to e_id/cow, as it is the only available cereal,
            # the other cereal (v) is already assigned!
            cow_orders.append(e_id)

def remove_edges(cow_id):
    # cow_id is the same as edge id
    f,s = cows[cow_id]    
    removed_edge.add(cow_id)
    # need to keep other parallel edges
    
removed_edge = set() # to break cycles in bfs_find_permutation, need to remove some edges
visited = [0] * (M+1)
for i in range(M+1):
    if visited[i] or not graph[i]:
        continue # if vertex has been visited or has No edge
    cow_id = bfs_find_cycle(i)
    if cow_id:
        f,s = cows[cow_id]
        cow_orders.append(cow_id)
        remove_edges(cow_id) # cow_id is the same as edge id, and assign cereal f to cow_id
        # break the cycle
        # the idea is to make the searching/start vertex unavailbe, so the cow/edge must use the other vertex 
        bfs_find_permutation(f)
        # print(f'Cycle with {f=}')
        # print(cow_orders)
    else:
        bfs_find_permutation(i)
        # print(f'No cycle with {i=}')
        # print(cow_orders)

print(N-len(cow_orders))

order_str = '\n'.join((str(x) for x in cow_orders))

cow_orders_set = set(cow_orders)
hungry_cows = [i for i in range(1, N+1) if i not in cow_orders_set]
hungry_cows_sr = '\n'.join((str(x) for x in hungry_cows))

print(order_str)
print(hungry_cows_sr)

'''
from collections import deque
import os
import sys

N, M = [int(x) for x in input().split()]
#print(N,M)

cereals = [ list() for _ in range(M+1)] 
cows = dict()

# cows_list / cows_assigned_set are to verify results
cows_list = list() 
cows_list.append((-1,-1))
cereal_assigned_dic = dict()
cows_dict = dict()
vertices = [dict() for i in range(M+1)]

for i in range(N):
    cereal_1,cereal_2 = [int(x) for x in input().split()]
    cows_list.append((cereal_1, cereal_2))
    if vertices[cereal_1].get(cereal_2,0) >= 2:
        #print(f"Already 2 cows (edges) for {cereal_1} {cereal_1}")
        continue
    vertices[cereal_1][cereal_2] = vertices[cereal_1].get(cereal_2,0) + 1
    vertices[cereal_2][cereal_1] = vertices[cereal_2].get(cereal_1,0) + 1
    if (cereal_1,cereal_2) not in cows:
        cows[(cereal_1,cereal_2)] = list()
    cows[(cereal_1,cereal_2)].append(i+1)
    
#print(vertices)
#print(cows)

vertice_visit = [0] * (M+1)
cow_orders = list()

def assign_cereal(cow):
    c1, c2 = cows_list[cow]
    if c1 not in cereal_assigned_dic:
        cereal_assigned_dic[c1] = cow
        return (c1,c2)
    if c2 not in cereal_assigned_dic:
        cereal_assigned_dic[c1] = cow
        return (c2,c1)
    return (-1,-1)            
    
def add_cow(i,j):
    try:
        if (i,j) in cows:
            cow = cows[(i,j)][-1]
            cows[(i,j)].pop()
            if len(cows[(i,j)]) == 0: cows.pop((i,j))             
        else:
            cow = cows[(j,i)][-1]
            cows[(j,i)].pop()
            if len(cows[(j,i)]) == 0: cows.pop((j,i))
    except IndexError:
        #print(f' {i=} {j=} {cows[(i,j)]=}')
        sys.exit()
        
    cow_orders.append(cow)
    c = assign_cereal(cow)
    return c
    
def bfs_loops(i):
    que = deque()
    que.append((i,-1))
    temp_visited = [0] * (M+1) 
    temp_visited[i] = 1
    vist_cnt = 1
    while len(que) > 0:
        k,parent = que.popleft()
        # get all edges of vertices[k]
        neighbors = []
        for key, val in vertices[k].items():
            neighbors += [key]*val
        for j in neighbors:
            if temp_visited[j] == 0:
                que.append((j,k))
                temp_visited[j] = 1
                vist_cnt+=1
            elif j != parent:
                c = add_cow(k,j)
                vertices[k][j] -=1
                vertices[j][k] -=1
                return (*c, vist_cnt) # (cereal_assigned, not_assigned, vist_cnt)
    return (None, None, vist_cnt)

def bfs_orders(i, p):
    #print(f'call bfs_orders {i=} {p=}')    
    loop_detected = False
    que = deque()
    que.append((i,p))
    vertice_visit[i] = 1
    cnt = 1
    while len(que) > 0:
        k,parent = que.popleft()
        # get all edges of vertices[k]
        neighbors = []
        for key, val in vertices[k].items():
            neighbors += [key]*val
        for j in neighbors:
            if vertice_visit[j] == 1:
                if j != parent: loop_detected = True
            elif j != parent:
                que.append((j,k))
                vertice_visit[j] = 1
                cnt += 1
                add_cow(k,j)
                
    if loop_detected == False: cnt -= 1
    return cnt

for i in range(1,M+1):
    #print(f'vertice(cereal) {i=} {vertice_visit[i]=}')
    if vertice_visit[i] == 1: continue
    x = bfs_loops(i)
    #print(f'cereal {i=} loop_detect return {x=}')
    if x[0] is not None:
        bfs_orders(x[0], -1)
    else:
        bfs_orders(i,-1)
            
print(N-len(cow_orders))

cow_added = [0]*(N+1)
for m in cow_orders:
    print(m)
    cow_added[m] = 1 
    
for i in range(1,(N+1)):
    if cow_added[i] == 0:
        print(i)
'''
