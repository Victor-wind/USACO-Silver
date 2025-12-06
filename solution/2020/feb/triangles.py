# All tests complete within 500 ms.

with open('triangles.in') as f:
    N = int(f.readline())
    points = [[int(x) for x in f.readline().split()] for _ in range(N)]

# print(N)
points.sort() # sort points based on x-axis, then based on y-axis (for the same x)

grid = list()
x_lst = [(points[0])]
for i in range(1, len(points)):
    if points[i][0] != points[i-1][0]:
        grid.append(x_lst)
        x_lst = list()
    x_lst.append(points[i])
grid.append(x_lst)

# To calculate sum(|Xi-Xj|) for every i, j.
# First computer S_0=sum(|Xi-X0|) for each i in X1 < X2 < X3 ... < Xn-1
# Then for all 1<i<N-1, S_i=S_i-1 + (2i-N)*(Xi-Xi-1)   <- for i = 0, 1, 2, ..., i-1, S_i = S_i-1 + i*(Xi-Xi-1)
#                                                         for i = i, i+1, ..., N-1,  S_i = S_i-1 - (N-i)*(Xi-Xi-1)
for x_lst in grid:
    lst = [point[1] for point in x_lst]
    n = len(x_lst)
    s_0 = sum(lst) - n*lst[0]
    x_lst[0].append(s_0)
    for j in range(1,n):
        s_j = x_lst[j-1][-1] + (lst[j] - lst[j-1]) * (2*j-n)
        x_lst[j].append(s_j)

y_hash = dict()
for point in points:
    x, y, _ = point
    y_lst = y_hash.get(y,list())
    y_lst.append(point)
    y_hash[y] = y_lst
# print(y_hash)

# To calculate sum(|Yi-Yj|) for every i, j. The same as X in lines 20 -32
for key, points_lst in y_hash.items():
    # print(f'{key=} {points_lst=}')
    y_lst = [point[0] for point in points_lst]
    n = len(y_lst)
    s_0 = sum(y_lst) - n * y_lst[0]
    points_lst[0].append(s_0)
    for j in range(1, n):
        s_j = points_lst[j - 1][-1] + (y_lst[j] - y_lst[j - 1]) * (2 * j - n)
        points_lst[j].append(s_j)

# print(f'{grid=}')
mod = 1000_000_000 + 7
result = 0
for point in points:
    rectangle_size = point[-1]*point[-2]
    if point[-2] < 0 or point[-1] < 0: print(f'Error! {point[-1]} {point[-2]}')
    result = (result + rectangle_size) % mod

print(f'{result}')

with open("triangles.out", "w") as f:
    f.write(f'{result}\n')

