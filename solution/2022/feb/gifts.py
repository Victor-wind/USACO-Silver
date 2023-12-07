
'''
 Submitted; Results below show the outcome for each judge test case
*
1             2        3        4       5         6       7        8       9        10      11  
10.6mb      10.6mb    10.6mb   17.7mb   18.0mb   18.2mb   17.7mb   18.2mb  18.1mb   18.0mb  18.4mb
67ms        68ms      67ms     580ms    767ms    855ms    583ms    925ms   854ms    695ms   964ms
*
'''
from collections import deque

N = int(input())
'''
4
1 2 3 4
1 3 2 4
1 2 3 4
1 2 3 4
'''
cows = []
graph = []
reachable = list()

def bfsSearch(graph, i, reachable):
    visited = [0] * (N+1)
    q = deque()
    visited[i] = 1
    q.append(i)
    reachable[i][i] = 1
    while len(q) > 0:
        j =q.popleft()
        for k in graph[j]:
            if visited[k] == 0:
                q.append(k)
                reachable[i][k] =1
                visited[k] = 1
    return

for i in range(N+1):
    graph.append(list())
    reachable.append([0]*(N+1))
    reachable[i][i] = 1 # gift i is assigned to cow i
    
for i in range(N):
    x = [int(x) for x in input().split()]
    cow = i+1
    # build a graph, (i -> j) cow j could accept gift i
    for gift in x:
        graph[gift].append(cow)
        if gift == cow:
            break
    cows.append(x)

'''
in the graph, if there is a loop, all cows in the loop could get better gifts.
For example 1->5->6->1: Gift 1 is exchanged to Cow 5; Gift 5 is exchanged to Cow 6; Gift 6 is exchanged to Cow 1.
It works because initially Cow i has Gift i!
Use bfs search to find whether i could reach j. bfs is preferred in Python to avoid recursive calls.
Be aware that if i can reach j and j can reach i, does not necessarily mean there is a loop among i and j.
Example: loop1: 1->2->3->1; loop2: 4->2->3->4. loop 1 and loop 2 share a common edge 2->3.
         1 can reach 4 through 1->2->3->4; 4 can reach 1 through 4->2->3>4.
         But there is no simple loop among 1,4. 1->2->3->4->2->3->1. edge 2->3 passes twice!
For this question, it is not a problem, as it only needs to check direct link. 
'''
#print(f'{cows=}')

'''
The question asks for the best POSSIBLE gifts for each cow, not best gifts for ALL cows.
Take the example above loop1: 1->2->3->1; loop2: 4->2->3->4. loop 1 and loop 2 share a common edge 2->3.
For Cow 1, she can take gift 3; For Cow 4, she can take gift 3 too;
But gift 3 can’t be given to both Cow 1 and 4! 

'''
for i in range(1, N+1):
    bfsSearch(graph, i, reachable)

#print(f'{reachable=}')

for i in range(N):
    for k in cows[i]:
        if reachable[i+1][k] == 1:
            print(k)
            break
          
