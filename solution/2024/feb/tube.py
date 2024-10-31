# Only tests 10,20 time out; all other tests pass
def build_tube(tube, s):
    for x in s:
        x = int(x)
        if len(tube) == 0 or tube[-1] != x:
            tube.append(x)        

def single_tube(tube_from, tube_to, breaker, i, k):
    cnt = 0
    while len(tube_from) > 1:
        if tube_from[-1] == tube_to[-1]:
            moves.append(f'{i} {k}')            
        else:
            moves.append(f'{i} 3')
            if not breaker: breaker.append(tube_from[-1])
        tube_from.pop()
        cnt +=1
    return cnt
    
def move_water(first_tube, sec_tube, breaker):
    cnt = 0
    if len(first_tube) == 1 and len(sec_tube) == 1:
        return 0
    # both first_tube and sec_tube have >=2 water; impossible to have one tube with 1 water
    # as single_tube called first,
    # and first_tube[0]!=sec_tube[0]
    # Make the bottom water of the three tubes not the same
    if len(breaker) == 0:
        cnt +=1
        if first_tube[0] == sec_tube[0] and first_tube[0] == first_tube[-1]:
            moves.append(f'2 3')
            breaker.append(sec_tube[-1])
            sec_tube.pop()
        else:
            moves.append(f'1 3')
            breaker.append(first_tube[-1])
            first_tube.pop()
    while len(first_tube) > len(sec_tube): # len(sec_tube) > 1
        if first_tube[-1] == sec_tube[-1]: moves.append(f'1 2')
        else: moves.append(f'1 3')
        first_tube.pop()
        cnt +=1
    while len(sec_tube) > len(first_tube): # len(first_tube) > 1
        if sec_tube[-1] == first_tube[-1]: moves.append(f'2 1')
        else: moves.append(f'2 3')
        sec_tube.pop()
        cnt +=1
    # now len(first_tube) == len(sec_tube), pour water alternatively from first_tube and sec_tube.
    # the reason is to ensure either first_tube or sec_tube could pour water without changing breaker.
    # for example, 1: 212; 2: 121; 3:2; if empty first_tube, 1:2; 2:121; 3:2, we could not pour water
    # from the sec_tube without updating the breaker. This is not optimal. 
    # in the loop, either first_tube or sec_tube should reduce by 1
    while len(first_tube) > 1 or len(sec_tube) > 1:
        if len(first_tube) > 1:
            if first_tube[-1] == sec_tube[-1]:
                moves.append(f'1 2')
                first_tube.pop()
                cnt +=1
            elif first_tube[-1] == breaker[-1]:
                moves.append(f'1 3')
                first_tube.pop()
                cnt +=1
        if len(sec_tube) > 1:
            if sec_tube[-1] == first_tube[-1]:
                moves.append(f'2 1')
                sec_tube.pop()
                cnt +=1
            elif sec_tube[-1] == breaker[-1]:
                moves.append(f'2 3')
                sec_tube.pop()
                cnt +=1
    return cnt           
    
def water_pour(N, P, f, s):
    breaker = list()
    first_tube = list()
    sec_tube = list()
    build_tube(first_tube,f)
    build_tube(sec_tube,s)
    #print(f'{first_tube=}')
    #print(f'{sec_tube=}')   
    pours = 0
    
    #pre-process tube water: if top water is the same, pour tube 2 -> tube 1
    # or tube 1 -> tube 2
    if len(sec_tube) > 1 and first_tube[-1] == sec_tube[-1]:
        sec_tube.pop()
        pours = 1
        moves.append(f'2 1')
         
    #process special cases
    if len(first_tube) == 1:
        pours += single_tube(sec_tube, first_tube, breaker, 2, 1)
    if len(sec_tube) == 1:
        pours += single_tube(first_tube, sec_tube, breaker, 1, 2)
            
    # either first_tube, sec_tube, breaker has one item     
    # or first_tube/sec_tube >= 2 item and breaker has NO item 
    pours += move_water(first_tube, sec_tube, breaker)        
    
    # final process water
    if len(first_tube) > 0 and len(sec_tube) > 0 and first_tube[0] == sec_tube[0]:
        sec_tube.pop()
        pours += 1
        moves.append(f'2 1')
    if len(breaker) > 0:
        pours += 1
        if len(first_tube) == 0 or first_tube[0] == breaker[0]:
            moves.append(f'3 1')            
        if len(sec_tube) == 0 or sec_tube[0] == breaker[0]:
            moves.append(f'3 2')
        breaker.pop()
    print(pours)
    if P > 1:
        for move in moves: print(move)
    

T = int(input())
for _ in range(T):
    N, P = [int(x) for x in input().split()]
    f = input()
    s = input()
    moves = list()
    #print(f'{N=} {P=} \n {f} {s}')
    water_pour(N,P,f,s)

