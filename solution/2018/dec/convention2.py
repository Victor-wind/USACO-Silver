from queue import PriorityQueue

with open('convention2.in') as f:
    lines = f.readlines()

N = int(lines[0])
cows = [ [int(x) for x in line.split()] for line in lines[1:]]
for i in range(N):
    cows[i].append(i)

cows.sort() 
#print(f'{cows=}')
max_wait = 0
wait_queue = PriorityQueue()
i = 0
cur_time = cows[0][0]

while wait_queue and i < len(cows):
    # add to wait queue
    while i < len(cows) and cows[i][0] <= cur_time:
        wait_queue.put( (cows[i][2], cows[i]) )
        i += 1
        
    # no cow is waiting, move cur_time
    if wait_queue.empty():
        wait_queue.put( (cows[i][2], cows[i]) )
        cur_time = cows[i][0]
        i += 1
        
    # update cur_time
    x = wait_queue.get()
    wait_time = cur_time - x[1][0]
    max_wait = max(max_wait, wait_time)
    
    cur_time += x[1][1]
    

print(max_wait)            
with open('convention2.out','w') as f:
    f.write(f'{max_wait}\n')
   
