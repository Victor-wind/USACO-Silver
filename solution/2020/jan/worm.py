'''
All tests pass within 1300 ms
'''

f = open("wormsort.in","rb")

N, M = [int(x) for x in f.readline().split()]

print(f'{N} {M}')

cows = [int(x) for x in f.readline().split()]
#print(f'{cows}')

edges = list()
graph = [[] for _ in range(N)]
min_w = 1
max_w = 1000000001
weights = []
for i in range(M):
    a, b, w = [int(x) for x in f.readline().split()]
    # print(f'{a} {b} {w}')
    # edge = [a - 1, b - 1, w]
    # edges.append(edge)
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))
    min_w = min(min_w, w)
    max_w = max(max_w, w)
    weights.append(w)


# set union for all cows: find connected components
def get_root(i: int, root: list) -> int:
    while i != root[i]:
        i = root[i]
    return i


# use union to find connected components in graph
# time out for test case 6 -10
def valid_union(w: int, edges: list) -> bool:
    root = [i for i in range(N)]
    for e in edges:
        a, b, width = e
        if width >= w:
            root[get_root(a, root)] = get_root(b, root)

    for i in range(N):
        v = cows[i]
        v = v - 1
        # could v move to position v?
        # For example, cows[3] = 10, cow '9' (10-1) is at pos 3, could '9' move to pos 9?
        # if 3 and 9 are in the same group (union)- have the same root, YES.
        # for cows within the same connected component, you can sort them in any order
        # how? swap and move the 'leave' cows to the ends like bubble sort algorithm on a tree structure  
        if get_root(i, root) != get_root(v, root):
            return False
    return True


# use breadth first search
def valid_bfs(w: int, graph: list) -> bool:
    components = [-1] * N
    components_id = 0
    # use breadth first search to iterate the graph to find connected components,
    # each component is identified by id.
    # note: in the graph, a node is the index of cows list, not the value
    for i in range(N):
        if components[i] == -1:  # not visited before in the graph
            to_visit = [i]
            components[i] = components_id
            j = 0
            while j < len(to_visit):  # another option is to use queue to do breadth first search
                node = to_visit[j]
                for k, wid in graph[node]:
                    if components[k] == -1 and wid >= w:
                        components[k] = components_id
                        to_visit.append(k)
                j += 1
            components_id += 1
        #  components[i] should have a component id
        #  could the cow at index i move to position cows[i]?
        #  for example, cows[3] = 100, could the cow at pos 3 move to pos 99 (100)?
        #  if components[3] == components[99] (3, and 99 are in the same connected component) -> YES
        elif components[i] != components[cows[i]-1]:
            return False

    return True

'''
while min_w <= max_w:
    mid = (max_w + min_w) // 2
    # x = valid_union(mid, edges)
    x = valid_bfs(mid, graph)
    # print(f' {mid} {x}')
    if x:
        min_w = mid + 1
    else:
        max_w = mid - 1

if max_w == 1000000001:
    max_w = -1
print(max_w)
'''


weights.sort()
weights.append(10 ** 9 + 1)

lo, hi = 0, M 
while lo <= hi:
    mid = (lo + hi) // 2
    if valid_bfs(weights[mid], graph):
        lo = mid + 1
    else:
        hi = mid - 1

max_w = -1 if hi == M else weights[hi]
print(max_w)
with open('wormsort.out', 'w') as f:
    f.write(f'{max_w}\n')
