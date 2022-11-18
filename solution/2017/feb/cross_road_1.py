from queue import PriorityQueue

with open('helpcross.in') as f:
    lines = f.readlines()

C,N = [ int(x) for x in lines[0].split()]    

chickens = [int(x) for x in lines[1: 1+C]]
chickens.sort()

cows = [ [ int(i) for i in x.split()] for x in lines[1+C:]]
cows.sort()

#print(f'{chickens=}')
#print(f'{cows=}')

pq = PriorityQueue()
pairs = 0
cow_index = 0

for c in chickens:
    # add all cows (coming before chicken c) to pq
    while cow_index < N and  cows[cow_index][0] <= c:        
        # priority is cow's leave time
        # Select the cow who leaves first
        pq.put( cows[cow_index][1] )
        cow_index+=1

    # A1        B1             -> Cow1
    #     A2          B2       -> Cow2
    #               C
    # for chicken c, remove Cow1 (B1 < C) from queue, as it could not pair
    # Cow1 also could not pair with all chickens after C. It is safe to remove it 
    while not pq.empty():
        x = pq.get()
        if x >= c: # find the pair
            pairs += 1
            break        
    
print(pairs)            
with open('helpcross.out','w') as f:
    f.write(f'{pairs}\n')
    
    
   
