'''
 https://usaco.guide/problems/usaco-596-build-gates/solution 
 Submitted; Results below show the outcome for each judge test case
 1        2      3        4      5       6        7       8       9       10
 10.7mb  10.7mb  10.7mb  10.7mb  10.7mb  10.7mb   10.7mb  10.7mb  10.7mb  10.7mb
 177ms   182ms   182ms   185ms   175ms   189ms    180ms   189ms   183ms   179ms
''' 

from collections import deque

f = open('gates.in')

N = int(f.readline())
s = f.readline()
print(N)

def get_edge(vertex, vertex_2):
    x1, y1 = vertex
    x2, y2 = vertex_2
    if x1 < x2 or (x1==x2 and y1 <y2):
        return (x1,y1,x2,y2)
    else:
        return (x2,y2,x1,y1)

    
min_gates = 0
vertex = [0,0]

vertex_set = set()
edge_set = set()

vertex_set.add((0,0))
 
for i in range(N):
    x,y = vertex
    c = s[i]
    if c == 'N':
        y+=1
    if c == 'S':
        y-=1
    if c == 'E':
        x+=1
    if c == 'W':
        x-=1
        
    e = get_edge( (x,y), (vertex[0],vertex[1]))
    if (x,y) in vertex_set and e not in edge_set:
        min_gates += 1
    vertex_set.add((x,y))
    edge_set.add(e)
    
    vertex[0] = x
    vertex[1] = y            

print(min_gates)
with open('gates.out', 'w') as f:
    f.write(f'{min_gates}\n')
