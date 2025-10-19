# All test cases pass within 400 ms

from datetime import datetime

now = datetime.now(); current_time = now.strftime("%H:%M:%S"); print('0 ',current_time)

with open('meetings.in') as f:
    lines = f.readlines()

now = datetime.now(); current_time = now.strftime("%H:%M:%S"); print('1 ',current_time)

N, L = [int(x) for x in lines[0].split()]
cows = list()
total_weights = 0
for i in range(N):
    w, x, v = [int(x) for x in lines[i+1].split()]
    total_weights += w
    # print(f'{w} {x} {v}')
    cows.append([w, x, v])

# sort the cows list based on x (distance)
cows = sorted(cows, key=lambda cow: cow[1])

# in order to sort cows based on their distances to the barns, create another list [distance, index]
cows_dist = list()
for i in range(N):
    dist = L-cows[i][1] if cows[i][-1] == 1 else cows[i][1]
    cows_dist.append([dist, i])
cows_dist.sort()
# print(cows_dist)

# "At meeting, cow i is assigned cow j's previous velocity and vice versa".
# The above can be interpreted as "cow i and j continue with previous velocity, but exchange weights".
# So that it is very simple to calculate how long it takes for each cow reach the barn.
# The key observation: all cows keep their relative weights along the path, after the meeting.
# so the first cow reaching the left barn has weight cows[0][w],
# the second cow reaching the left barn has weight cows[1][w], and so on.
# Similar cases for cows reaching the right barn.
# Then we can find the T with cows in order.
T = total_weights/2
weights = 0
left_index = 0
right_index = -1
reached_cows_lst = list()
end_cow_index = N+1
for i in range(N):
    cow_index = cows_dist[i][1]
    velocity = cows[cow_index][-1]
    if velocity == -1:
        w = cows[left_index][0]
        left_index += 1
    else:
        w = cows[right_index][0]
        right_index -= 1
    weights += w
    reached_cows_lst.append(cow_index)
    if weights >= T:
        end_cow_index = cow_index
        break

max_dist_moved = L-cows[end_cow_index][1] if cows[end_cow_index][-1] == 1 else cows[end_cow_index][1]
# print('cows ={}'.format(cows))
# print(f'{total_weights=} {T=}')
# print(f'{reached_cows_lst=} {end_cow_index=} {len(reached_cows_lst)=}')
# print(f'{max_dist_moved=}')

# Determine how many meetings are needed for cows in reached_cows_lst
# maintain a sliding window with size 2*max_dist_moved.
# For each cow moving right, it will meet the cows moving left within the window.
cows_move_left = list()
cows_move_right = list()
for i in range(N):
    if cows[i][-1] == 1:
        cows_move_right.append(i)
    else:
        cows_move_left.append(i)

# print(f'DEBUG {cows_move_right=}')
# print(f'DEBUG {cows_move_left=}')


def debug_helper(i, N, pos, cows, debug=False):
    cnt = 0
    for j in range(N):
        if cows[j][-1] == -1 and pos >= cows[j][1] >= cows[i][1]:
            # if debug: print(f'  Meet with {j=} pos={cows[j][1]=} dir={cows[j][-1]=}')
            cnt += 1
    return cnt


now = datetime.now(); current_time = now.strftime("%H:%M:%S"); print('2 ',current_time)


result, total_meetings = (0, 0)
win_l = win_r = 0 # index of cows_move_left
max_win_r = len(cows_move_left)
k = 0 # k is the index of cows_move_left list, cows[cows_move_left[k]][1] is the location
for i in cows_move_right:
    # move the win_r towards right so win_r
    cnt = 0
    pos = cows[i][1] + max_dist_moved + max_dist_moved
    # print(f'Moving right {i=} {cows[i][1]=} {pos=}')
    # xyz = debug_helper(i, N, pos, cows)
    # move window right
    while win_r < max_win_r and cows[cows_move_left[win_r]][1] <= pos:
        win_r += 1
    # move window left
    while win_l < max_win_r and cows[cows_move_left[win_l]][1] < cows[i][1]:
        win_l += 1
    total_meetings += win_r - win_l
    ''' 
    result += xyz
    if xyz != (win_r - win_l):
        print(f'    {xyz=} {(win_r-win_l)=} {win_r=} {win_l}')
        debug_helper(i, N, pos, cows, True)
    '''

now = datetime.now(); current_time = now.strftime("%H:%M:%S"); print('3 ',current_time)
print('total_meetings={} result={}'.format(total_meetings, result))
with open('meetings.out', 'w') as f:
    f.write(f'{total_meetings}\n')


