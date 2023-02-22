from collections import deque

f = open('perimeter.in')

N = int(f.readline())

print(N)

grid = [ [-1]*(N+2) for _ in range(N+2)]
for i in range(N):
    s = f.readline()
    for j in range(N):
        if s[j] == '#':
            grid[i+1][j+1] = 0
        
#print(grid)
f.close()
cnt = 0

'''
def flood_fill(grid, cnt, i, j):
    if grid[i][j] != 0:
        return
    grid[i][j] = cnt
    flood_fill(grid, cnt, i+1, j)
    flood_fill(grid, cnt, i-1, j)
    flood_fill(grid, cnt, i, j+1)
    flood_fill(grid, cnt, i, j-1)
    
# RecursionError: maximum recursion depth exceeded in comparison
for i in range(1, N+1):
    for j in range(1, N+1):
        if grid[i][j] == 0:
            cnt += 1        
            flood_fill(grid, cnt, i, j)
'''
dirs = [(1,0), (-1,0), (0,1), (0, -1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if grid[i][j] == 0:
            cnt += 1            
            de = deque()            
            de.append((i,j))
            while len(de) > 0:
                m,n = de.popleft()
                if grid[m][n] != 0:
                    continue
                else:
                    grid[m][n] = cnt
                for d in dirs:
                    x = m+d[0]
                    y = n+d[1]
                    if grid[x][y] == 0:
                        de.append((x,y))
                

max_area, min_perimeter = 0, (N+1)*(N+1)
areas = [0] * (cnt+1)
perimeters = [0] * (cnt+1)


for i in range(1, N+1):
    for j in range(1, N+1):
        x = grid[i][j]
        if x > 0:
            areas[x] += 1        
            if grid[i+1][j] == -1: perimeters[x] += 1
            if grid[i-1][j] == -1: perimeters[x] += 1
            if grid[i][j+1] == -1: perimeters[x] += 1
            if grid[i][j-1] == -1: perimeters[x] += 1
            
max_area = max(areas)
for i in range(cnt+1):
    if areas[i] == max_area:
        min_perimeter = min(min_perimeter,perimeters[i])            


print(f'{max_area} {min_perimeter}')

with open('perimeter.out','w') as f:
    f.write(f'{max_area} {min_perimeter}\n')
