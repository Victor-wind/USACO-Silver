from queue import PriorityQueue

q = PriorityQueue()
with open('cowdance.in') as f:
    lines = f.readlines()

N, T_Max = [int(x) for x in lines[0].split()]
print(N, T_Max)

cows = [int(x) for x in lines[1:]]
#print(cows)

left = 1
right = N

def can_complete(cows:list, T_Max: int, k:int) -> bool:
    if k <= 0: return False

    pq = PriorityQueue()
    N = len(cows)
    i = 0
    cur_time = 0

    while i < k:
        i+=1
        pq.put(cows[i])

    while not pq.empty():
        x = pq.get()
        cur_time = x
        if i < N:
            pq.put(cows[i]+cur_time)
            i += 1
        if cur_time > T_Max:
            return False        
    
    return True

while left < right:
    mid = (left + right)//2
    if can_complete(cows, T_Max, mid):
        right = mid
    else:
        left = mid+1

print(right)
with open('cowdance.out','w') as f:
    f.write(f'{right}\n')
    
