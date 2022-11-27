
with open('angry.in') as f:
    lines = f.readlines()

N, K = [int(x) for x in lines[0].split()]
print(N,K)
hays = [int(x) for x in lines[1:]]
hays.sort()
p#rint(f'{hays=}')

def detonate_all(hays:list, r: int, K:int)->bool:
    n = len(hays)
    i = 0
    cnt = 0 # cnt is the # of cows needed to detonate all hay bales
    while i < n:
        cnt += 1
        range_r = hays[i]+r+r
        # all hay bales <= range_r can be detonated
        while i < n and hays[i] <= range_r:
            i += 1
    return cnt <= K

left  = 1
right = hays[-1]
# binary search the minimum power R
while left < right:
    mid = (left+right)//2
    if detonate_all(hays, mid, K):
        right = mid
    else:
        left = mid+1

print(left)
with open('angry.out','w') as f:
    f.write(f'{left}\n')
 
