with open('measurement.in') as f:
    lines = f.readlines()

N, G = [int(x) for x in lines[0].split()]
print(N,G)

logs = [ [ int(y) for y in x.split()] for x in lines[1:]]
logs.sort()

#print(logs)
#for x in logs: print(x)

cnt = 0
unknown  = []

highest_ouput = G
cows = dict()
pic = set()

    
def best_cows(cows):
    if not cows: return []

    values = list(cows.values())
    values.sort(reverse=True)
    
    res = [k for k, v in cows.items() if v == values[0]]
   
    return res
    
for log in logs:
    cow_id, adjust = log[1], log[2]
    output = cows.get(cow_id, G) + adjust
    cows[cow_id] = output
            
    if output == highest_ouput: # add it to pic
        cnt += 1
        pic.add(cow_id)
        #print(f'{log[0]=} {highest_ouput=} {pic=}')
    elif output > highest_ouput: # add it to pic
        highest_ouput = output

        next_cows = best_cows(cows)
        new_pic = set(next_cows)
        if pic != new_pic:
            cnt += 1
            pic = new_pic
    else:
        # corner case: at the beginning, all cows are in pic, as one cow is removed, need to update pic
        # but the pic is still unkown 
        if not pic:
            cnt +=1
            continue
        
        if cow_id not in pic: # do not need to remove from pic
            continue
        #print(f'DEBUG {log=} ')
        next_cows = best_cows(cows)
        new_pic = set(next_cows)
        
        # one corner case the pic should not change:
        # the cow is the only one, and even reduces output, it still the best producer               
        if pic == new_pic:
            highest_ouput = cows[cow_id]
            continue
        
        cnt += 1
        pic = new_pic
        highest_ouput = cows[next_cows[0]]
        #print(f'{log[0]=} {highest_ouput=} {pic=} {next_cows=} ')        
                
print(cnt)            
with open('measurement.out','w') as f:
    f.write(f'{cnt}\n')
    
