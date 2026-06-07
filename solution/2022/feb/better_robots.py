
'''
*  
1         2        3       4        5         6        7         8       9          10      11       12        13        14       15        16
10.7mb   10.7mb  10.7mb   10.7mb    10.7mb   11.0mb  64.1mb  389.1mb  438.6mb   439.1mb   439.1mb  439.1mb   439.1mb  443.1mb  239.6mb   10.7mb
69ms     72ms     71ms    81ms      2952ms   2758ms  3134ms  4383ms   4452ms    4803ms    4486ms   4677ms    4501ms   4523ms   3265ms    1792ms
*
'''


from collections import defaultdict, Counter
import sys

input = sys.stdin.readline

N = int(input())
xg, yg = map(int, input().split())

a = [tuple(map(int, input().split())) for _ in range(N)]

m = N // 2
L = a[:m]
R = a[m:]

right_map = defaultdict(Counter)

def dfs_right(i, sx, sy, cnt):
    if i == len(R):
        right_map[(sx, sy)][cnt] += 1
        return

    x, y = R[i]

    dfs_right(i + 1, sx, sy, cnt)
    dfs_right(i + 1, sx + x, sy + y, cnt + 1)

dfs_right(0, 0, 0, 0)

ans = [0] * (N + 1)

def dfs_left(i, sx, sy, cnt):
    if i == len(L):
        need = (xg - sx, yg - sy)

        vec = right_map.get(need)
        if vec:
            for rsz, ways in vec.items():
                ans[cnt + rsz] += ways
        return

    x, y = L[i]

    dfs_left(i + 1, sx, sy, cnt)
    dfs_left(i + 1, sx + x, sy + y, cnt + 1)

dfs_left(0, 0, 0, 0)

sys.stdout.write("\n".join(map(str, ans[1:])))