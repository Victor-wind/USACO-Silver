import sys, math

with open('revegetate.in') as f:
    lines = f.readlines()

N, M = [ int(x) for x in lines[0].split()]

graph = list()
for _ in range(N+1):
    graph.append(list())
   

#print(f'{N=} {M=}')
for i in range(M):
    converted = lines[i+1].split()
    x,y = [int(converted[1]), int(converted[2])]
    # build graph: pastures are nodes, cows are edges.
    # connected nodes are components in graph. If there are K components,
    # then the number of different ways to plant grass are 2**K.
    # explan: in one component, there are only 2 ways to plant grass.
    # for example 1 - (D) - 2 - (S) -3 -> [ 1(A) 2(B) 3(B)] or [1(B) 2(A) 3(A)]
    # if choose one node A/B, then all other nodes have only one choice.
    if converted[0] == 'S':
        graph[x].append(y)
        graph[y].append(x)
    else:
        # use negative to indicate two pastures have different grass.
        # positive and negative are used to determine whether it is possible to plant grass 
        graph[x].append(-y)
        graph[y].append(-x)

#print(graph)

visited = [0] * (N+1)
components = 0
impossible = False

for i in range(1, N+1):
    if visited[i] != 0:
        continue   

    neighbors = [i]
    components +=1
    visited[i] = 1 # color i to 1 to detect whether it has conflicts 1 -(s) 2 - (s) 3 - (d) 1

    # Queue also works. 
    while len(neighbors) > 0:
        temp = []        
        for j in neighbors:
            abs_j = abs(j)
            for k in graph[abs_j]:
                to_color = visited[abs_j] if k > 0 else -visited[abs_j]
                if visited[abs(k)] == 0:
                    temp.append(k)
                    visited[abs(k)] = to_color
                else:
                    if visited[abs(k)] != to_color:
                        impossible = True
                        
        neighbors = temp

res = '1' + '0'*components
if impossible:
    res = '0'
    
print(f' {components} {res}')
with open('revegetate.out','w') as f:
    f.write(f'{res}\n')
