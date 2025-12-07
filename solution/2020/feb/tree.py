# All tests complete within 100 ms.

# The official explanation is NOT for normal people to understand. 
# Key observation: There are N rooms (nodes) and N−1 corridors (edges), and it is possible to walk from any room to any other room.
# This implies that the 1. The graph is a tree, so there are no cycles; 2. There is exactly one unique path between any two nodes.
# 3. The graph is bipartite: from any node i, its direct neighbors belong to one set, their neighbors belong to the other set (which includes i), and so on
# No matter what room/node i Bessie starts from, the bipartite sets contain exactly the same rooms! This coclusion comes from observation 1 and 2. 
# Even if Bessie walks back and forth along the paths multiple times, the 2 room sets never change!
# Solution: Bessie starts at any room/node i, dfs walks through all rooms. To make the clocks to be 12 for the leaves / the end rooms, 
# the only way is to walk back and forth between the leaves and their parent room, which increase their clocks by the same value. 
# After the leaves's clock become 12, their direct parents become new "leaves". Do the same, until the dfs search returns to the start node i. 
# Optimization: 1. when reaching "leaves" room, Bessie can directly add the required value to its parent room.  
#                  If Bessie tries this approach from each of the N possible starting nodes, the complexity is O(N^2)
#                2. We can apply the observation 3. Rooms in the same bipartite set give the same result,so only need to conduct dfs search once. Why, look at the linear example. 
#                   ...1--2--3--4  When reach end romm 4, add 12-c(4) to its parent room 3, so room 3's clock becomes c(3) + 12 - c(4), 
#                   room 3 becomes end room, add 12-(c(3)+12-c(4)) to its parent room 2,  so room 2's clock becomes c(2)+c(4)-c(3) +12k ,
#                   when reaching room 1, room 1's clock becomes  c(1) + c(3) - c(2) - c(4)- +12k
#                   After returning to the start node i, simply compare the total effects on the two bipartite sets. Importantly, these two sets of rooms are fixed, no matter which room to start from.

with open('clocktree.in') as f:
    N = int(f.readline())
    clocks = [int(i) for i in f.readline().split()]
    grid = [ list() for i in range(N+1)]
    for _ in range(N-1):
        a, b = [int(i) for i in f.readline().split()]
        grid[a].append(b)
        grid[b].append(a)

print(N)
print(clocks)
# print(grid)
lst_1 = []
lst_2 = []
sum_1 = 0
sum_2 = 0


def dfs_search(i, color, parent, odd_lst, even_lst):
    global sum_1, sum_2
    if color == 1:
        odd_lst.append(i)
        sum_1 += clocks[i-1]
    else:
        even_lst.append(i)
        sum_2 += clocks[i - 1]
    # print(f'Visit room {i}')
    for child in grid[i]:
        if child == parent: continue
        dfs_search(child, -color, i, odd_lst, even_lst)


dfs_search(1, 1, 0, lst_1, lst_2)
# print(f'{lst_1=}')
# print(f'{lst_2=}')
result = 0
if sum_1 % 12  == sum_2 % 12:
    result = N
elif (sum_1 + 1) % 12 == sum_2 % 12:
    result = len(lst_2)
elif (sum_2 + 1) % 12 == sum_1 % 12:
    result = len(lst_1)

print(result)
with open("clocktree.out", "w") as f:
    f.write(f'{result}\n')
