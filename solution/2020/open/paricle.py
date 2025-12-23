# All tests pass within 400 ms

# Treat particles as Nodes and connect them with Edges if they spin. So We can build a graph. 
# The graph can be divided into multiple connected components. 
# For a given connected component, from ANY node (root), we can build a full connected tree.
# For the tree, start from the end nodes (leaves), we can remove the end nodes along the path until the root. 
# So each connected components has one root node (particle) left. 
# If we know the number of connected components, then we get the results. 
# To find the connected components, we can use dfs search with O(N) complexity.
# However, to build the graph, the normal way needs O(N^2) complexity. We need to do better.\
#
# Here a few characteristics of this particular graph that help to find a O(NlgN) solution.
# 1. The bottom node cannot be rightmost node, and the top node cannot be the leftmost node. Otherwise, there are No edges for them within a component.
#
#
# ------------------O (A)
#                   |
#                   |
#              O (D)|
# ------------------|-------- O (B)
#                   |         |
#                  O (C)      |
#                   |         |
#
# 2. "Sort" the components along x-axis, for component i, it has D-X_Min(i), B-X_Max(i), C-Y_Min(i), A-Y_Max(i) nodes
# 3. For component i and its next right component (i+1),  Y_Min(i) < Y_Max(i+1), so component (i+1) is at right bottom side of component i.
#     Any node M in component (i+1) and node N in component i:  M(x) > N(x) <-  component (i+1) is on the right side of component i.
#     If M(y) >=  N(y), there is an edge between M, N connecting component i and i+1. So component i and i+1 are not separated.
# 4. Is it possible that one node M in component (i+1) <= component (i) x-axis? No! Bellow is why
#    Suppose there is a node M in component (i+1), but M_x <= B-X_Max(i) of component i.
#    a. It cannot be placed in the rectangle topright with B and A. Otherwise, it can be connected to A or B.
#    b. Could it be placed in the rectangle of topleft A and botterright B? still No. Because A, B sub_components needs to be connected
#       by another node X, whose x <= A, and y <= B. However, X should be able to connect with M in the rectangle.
#    c. The only possible place to place M is on the lef of D and top of A. However, because of (2), M could not be connected to
#       any node in component (i+1), which is on the right side of component i.
#
# Now now we can get O(NlgN) solution.
# 1. Sort nodes in a list based on X, then Y. O(NlgN)
# 2. From the list, take node M from the list one by one. First, make M a seperate component.
# 3. Backward combine M with previous components if possible. As M_X >= all processed nodes, only need to compare M_Y with previous components' bottom.

with open('moop.in') as f:
    N = int(f.readline())
    particles = [ [int(x) for x in f.readline().split()] for _ in range(N)]

particles.sort()
print(N)
#print(particles)
components = list()

# index i is component's id,
# components[i] stores the smallest y of all particles in component i
components.append(particles[0][-1])
last_id = 0 
for i in range(1, N):
    y = particles[i][1]
    last_id = len(components)
    # add particles[i] as a single particle component 
    components.append(y)
    # could it combine with previous components?
    # print(f'Debug {i=} {y=} {components[-2]=}')
    while len(components) > 1 and y >= components[-2]:
        components[-2] = min(components[-1],components[-2]) 
        components.pop()
        last_id = len(components)-2
        
result = len(components)
print(result)
with open('moop.out', 'w') as f:
    f.write(f'{result}\n')
