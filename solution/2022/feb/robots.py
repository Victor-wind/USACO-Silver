
'''
*  
1         2        3       4        5         6        7         8       9          10      11       12        13        14       15        16
12.7mb   12.7mb  12.7mb   12.7mb    137.6mb   194.9mb  210.5mb  556.7mb  605.4mb   605.8mb   624.4mb  624.5mb   624.4mb  630.5mb  421.4mb   216.7mb
69ms     72ms     71ms    81ms      5548ms    6050ms   6407ms   5104ms   4668ms    4803ms    4726ms   4677ms    4687ms   4805ms   3715ms    5949ms
*
'''

from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
xg, yg = map(int, input().split())

a = [tuple(map(int, input().split())) for _ in range(N)]

m = N // 2
L = a[:m]
R = a[m:]

right_map = defaultdict(lambda: [0] * (len(R) + 1))

cur = [(0, 0, 0)]  # sx, sy, size

for x, y in R:
    nxt = []
    for sx, sy, sz in cur:
        nxt.append((sx, sy, sz))
        nxt.append((sx + x, sy + y, sz + 1))
    cur = nxt

for sx, sy, sz in cur:
    right_map[(sx, sy)][sz] += 1

ans = [0] * (N + 1)

cur = [(0, 0, 0)]

for x, y in L:
    nxt = []
    for sx, sy, sz in cur:
        nxt.append((sx, sy, sz))
        nxt.append((sx + x, sy + y, sz + 1))
    cur = nxt

for sx, sy, sz in cur:
    vec = right_map.get((xg - sx, yg - sy))
    if vec:
        for rsz, cnt in enumerate(vec):
            ans[sz + rsz] += cnt

sys.stdout.write("\n".join(map(str, ans[1:])))
