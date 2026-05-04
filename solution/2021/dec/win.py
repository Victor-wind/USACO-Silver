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


'''
import string
import time

start_time = time.time()

K, M, N = [ int(x) for x in input().split()]
patches = [ [int(x) for x in input().split()] for _ in range(K)]
cows = [ int(input()) for _ in range(M) ]

patches.sort()
cows.sort()

#print(f'{K=} {M=} {N=}')
#print(patches)
#print(cows)

tastiness_lst = list()

total_tastiness = 0
patch_s = 0
patch_end = K-1
# total_tastiness before the Nhoj's first cow
for i in range(K):
    if patches[i][0] > cows[0]:
        break
    total_tastiness += patches[i][1]
patch_s = i
if total_tastiness > 0:
    tastiness_lst.append(total_tastiness)
    
total_tastiness = 0
# total_tastiness after the Nhoj's last cow
for i in range(K-1, -1, -1):
    if patches[i][0] < cows[-1]:
        break
    total_tastiness += patches[i][1]
patch_end = i
if total_tastiness > 0:
    tastiness_lst.append(total_tastiness)

# print(f'Before the loop {tastiness_lst=}')
# consider each interval between Nhoj's cow i and cow i+1
# although 3 nested loops, the complexity is O(N), as each patch only visits Once.

# for any position q to put cow in interval (fx−1,fx) the window size is fixed: ( (fx−1+q)/2 , (fx+q)/2) ) -> (fx-fx-1)/2
# so here are 2 solutions
# a. Iternate all patches within interval (fx−1,fx). Let the left window be patch x. Slide/Resize the window to find the largest tastiness. 
# b. Iternate all patches within interval (fx−1,fx). Put the cow in the best pos, the calculate largest tastiness within the slide window
# AI doesn't like/understand solution (b). And solution a is easier to code.
for j in range(M-1):
    x = patch_s    
    if x > patch_end: break
    if patches[x][0] > cows[j+1]: continue
    if patches[x][0] < cows[j]:
        print(f"wrong patch moves {x} {j}")
        exit(1)    
    
    y = patch_s
    total_tastiness = 0 # total tastiness if adding 2 cows
    one_tastiness = 0 # best tastiness if adding only 1 cows
    one_tastiness_lst = list()
    win_size = cows[j+1] - cows[j]
    
    while x <= patch_end and patches[x][0] < cows[j+1]:
        
        total_tastiness += patches[x][1]
        while y <= patch_end and patches[y][0] < cows[j+1] and (patches[y][0]-patches[x][0])*2 < win_size:
            one_tastiness += patches[y][1]
            y += 1
        one_tastiness_lst.append(one_tastiness)
        # remove the tastiness of x for the next loop
        one_tastiness -= patches[x][1]
        x += 1        

    max_one_tastiness = max(one_tastiness_lst)
    patch_s = x
    tastiness_lst.append(max_one_tastiness)
    tastiness_lst.append(total_tastiness - max_one_tastiness)
    # print(f'{j=} {total_tastiness=} {one_tastiness_lst=}')

# print(f'after the loop {tastiness_lst=}')        
tastiness_lst.sort(reverse=True)
result = sum(tastiness_lst[:N])
print(result)

end_time = time.time()
# print(end_time - start_time) 

'''
