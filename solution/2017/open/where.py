'''
Submitted; Results below show the outcome for each judge test case
1        2       3       4       5       6       7        8   9       10
10.6mb   10.6mb  10.6mb  10.6mb  10.6mb  10.6mb  10.6mb   t   10.6mb  10.6mb
181ms    172ms   274ms   220ms   1489ms  444ms   623ms        974ms   984ms 
'''

from collections import deque

f = open('where.in')

N = int(f.readline())
#print(N)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

grid = list()
for i in range(N):
    s = f.readline()
    grid.append(s)

cnt_plc = 0


def is_plc(grid: list, u_left: list, b_right: list) -> bool:
    color_set = set()
    for i in range(u_left[0], b_right[0] + 1):
        for j in range(u_left[1], b_right[1] + 1):
            color_set.add(grid[i][j])
    if len(color_set) != 2:
        return False

    #print(f'{color_set=}')
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    color_cnt = dict()
    for i in range(u_left[0], b_right[0] + 1):
        for j in range(u_left[1], b_right[1] + 1):
            if visited[i][j] != 0:
                continue
           
            cnt += 1
            color = grid[i][j]
            color_cnt[color] = color_cnt.get(color, 0) + 1

            q = deque()
            q.append((i, j))
            while len(q) > 0:
                x, y = q.popleft()
                if visited[x][y] > 0: continue
                visited[x][y] = 1

                for d in dirs:
                    next_x, next_y = x + d[0], y + d[1]
                    if next_x < u_left[0] or next_x > b_right[0]: continue
                    if next_y < u_left[1] or next_y > b_right[1]: continue
                    if grid[next_x][next_y] != grid[i][j]: continue
                    if visited[next_x][next_y] != 0: continue
                    # visited[next_x][next_y] = 1                                        
                    q.append((next_x, next_y))

                    # verify is_plc by color_cnt
    v = list(color_cnt.values())
    v.sort()
    # the first component should have cnt == 1, the second should have cnt >=2 
    if len(v) != 2 or v[0] != 1 or v[1] < 2:
        return False
    return True

plc_list = list()
for i in range(N):
    for j in range(N):
        u_left = (i, j)
        for k in range(N-1,i-1,-1):
            for l in range(N-1,j-1,-1):
                b_right = (k, l)
                # for rectangular u_left, b_right
                valid = is_plc(grid, u_left, b_right)
                if valid:
                    # print(u_left, b_right)
                    plc_list.append((u_left, b_right))
                    # do not need to check other l, as they are inside (u_left, b_right) 
                    break
                
plc_list_size = len(plc_list)
# check whether one plc is inside of other plcs 
for i in range(plc_list_size):
    u_left, b_right = plc_list[i]
    plc_valid = True
    for j in range(plc_list_size):
        if i == j: continue 
        u_left_2, b_right_2 = plc_list[j]
        if u_left_2[0]<=u_left[0] and u_left_2[1]<=u_left[1] and b_right_2[0]>=b_right[0] and b_right_2[1]>=b_right[1]:
            plc_valid = False
            break
    if plc_valid:
        #print(f"valid {u_left=} {b_right=}")
        cnt_plc += 1
        
print(cnt_plc)
with open('where.out', 'w') as f:
    f.write(f'{cnt_plc}\n')
