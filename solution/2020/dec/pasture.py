# time out for test cases 13 - 20
# double loops for N =2500 O(N^2) takes 4 secondst. 2D Fenwick Tree for prefix sum doesn't help with the main N^2 loop
import sys
from datetime import datetime

N = int(sys.stdin.readline())
#print(N)
coordinates  = [ [int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
coordinates.sort()
x_map = { coordinates[i][0]:i for i in range(N)}
    
coordinates.sort(key=lambda x: x[1])
y_map = { coordinates[i][1]:i for i in range(N)}

compressed_grid = [ [0] * (N+1) for _ in range(N+1)]
points = list()

# after compression, each point has uniqure x, y
for x, y in coordinates:
    j = x_map[x]
    k = y_map[y]
    compressed_grid[j][k] = 1
    points.append((j,k))

prefix_grid = [ [0] * (N+1) for _ in range(N+1)]

v = 0
for i in range(N):
    v += compressed_grid[0][i]
    prefix_grid[0][i] = v
    # print(f'{prefix_grid[0][i]=}')
for i in range(1, N, 1):
    v = 0 
    for j in range(N):
        v += compressed_grid[i][j]
        # print(f'{i=} {j=} {v=} {prefix_grid[i-1][j]=}')
        prefix_grid[i][j] = prefix_grid[i-1][j] + v

# for all points pairs  
points.sort()
#print(points)

start_time = datetime.now()
rec_sum = 0
v1,v2 = (0,0)
for i in range(N):
    for j in range(i+1, N):
        p1 = points[i]
        p2 = points[j]        
        x1 = min(p1[0],p2[0])
        x2 = max(p1[0],p2[0])
        y1 = min(p1[1],p2[1])
        y2 = max(p1[1],p2[1])        
        # how many points are below y1 and within [x1,x2] inclusively
        v1 = prefix_grid[x2][y1] - prefix_grid[x1-1][y1]
        # how many points are above y2 and within [x1,x2] inclusively
        v2_1 = prefix_grid[x2][N-1] - prefix_grid[x1-1][N-1]
        v2_2 = prefix_grid[x2][y2] - prefix_grid[x1-1][y2]
        v2 = v2_1-v2_2+1
        rec_sum += v1*v2        
        #print(p1,p2,x)
print(rec_sum+1+N)

end_time = datetime.now()
time_difference = end_time - start_time
# print(time_difference)

        
