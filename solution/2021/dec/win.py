# All tests pass within 1300 ms

import sys

# read input
K, M, N = [int(x) for x in sys.stdin.readline().strip().split()]

if K <= 0 or M <= 0 or N <= 0:
    print("wrong input")
    exit(1)

patches = []
for _ in range(K):
    patches.append([int(x) for x in sys.stdin.readline().strip().split()])
patches.sort()  # sort by position

nhoj_cow = [int(sys.stdin.readline().strip()) for _ in range(M)]
nhoj_cow.sort()

tastiness_1 = []

# sliding window to compute max tastiness for one cow in interval
def cal_max_one_cow(k, i, j):
    max_tastiness = 0
    tastiness = 0

    win = nhoj_cow[k+1] - nhoj_cow[k]  # integer arithmetic
    left_idx = i
    for x in range(i, j):
        tastiness += patches[x][1]
        while 2 * (patches[x][0] - patches[left_idx][0]) >= win:
            tastiness -= patches[left_idx][1]
            left_idx += 1
        max_tastiness = max(max_tastiness, tastiness)

    return max_tastiness

def solution():
    j = 0  # pointer over patches

    # left segment (before first Nhoj cow)
    tastiness = 0
    while j < K and patches[j][0] < nhoj_cow[0]:
        tastiness += patches[j][1]
        j += 1
    tastiness_1.append(tastiness)

    # middle segments (between Nhoj cows)
    for i in range(M-1):
        start_idx = j
        while j < K and patches[j][0] < nhoj_cow[i+1]:
            j += 1
        if start_idx < j:  # there are patches in this interval
            total = sum(p[1] for p in patches[start_idx:j])
            # 2 cows can take all
            tastiness_one_cow = cal_max_one_cow(i, start_idx, j)
            tastiness_1.append(tastiness_one_cow)
            tastiness_1.append(total - tastiness_one_cow)

    # right segment (after last Nhoj cow)
    if j < K:
        tastiness = sum(p[1] for p in patches[j:])
        tastiness_1.append(tastiness)

    # pick N largest contributions
    tastiness_1.sort(reverse=True)
    sum_tastiness = sum(tastiness_1[:N])
    print(sum_tastiness)

solution()
