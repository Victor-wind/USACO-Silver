# All tests pass within 1200 ms

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
# The greedy approach is equivalent to the solution as stated “A solution with D greater than 0 is guaranteed to exist.”
# Suppose the solution places the cows at positions S1, S2, ... Sn on the line. 
# Step 1: Move cow 1 from S1 to the leftmost valid position G1 in the allowed interval. So G1<=S1, -> (S2-G1)>=(S2-S1)>=D;
# Step 2: Move cow 2 from S2 to the left as much as possible G2. So G2<=S2, and (G2-G1)>=D, -> (S3-G2) >= (S3-S2)>=D
# Continue this process for all cows.
# In the end, the sequence S1, S2, ... Sn becomes G1, G2, ... Gn, and the new positions still satisfy all the required distance constraints.
# Thus, the greedy method produces a valid solution equivalent to the original one.
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
