'''
with open('socdist.in') as f:
    lines = f.readlines()

N, M = [int(x) for x in lines[0].split()]
print(N,M)

intervals = [ [int(i) for i in x.split()] for x in lines[1:]]
intervals.sort()
#print(f'{intervals=}')
'''

# this runs faster than the above
with open('socdist.in', 'r') as r:
	N, M = [ int(x) for x in r.readline().split()]
	intervals = [tuple(map(int, r.readline().split())) for _ in range(M)]
	
intervals.sort()
	
# check whether can places N cows with distance d
def check_dist(N: int, d: int) -> bool:
    cnt = 1
    pos = intervals[0][0]
    for interval in intervals:        
        while pos+d <= interval[1]:
            pos = max(pos+d, interval[0])
            cnt += 1
            if cnt >= N:
                return True               
    return cnt >= N

left = 1
right = intervals[-1][1] - intervals[0][0]

# when d is small enough, FJ can place N cows
# find the smallest d, which could not place N cows. The result is d-1
while left < right:
    mid = (left+right)//2
    if check_dist(N, mid) :
        left = mid+1
    else:
        right = mid

res = left -1
print(res)

with open('socdist.out','w') as f:
    f.write(f'{res}\n')
