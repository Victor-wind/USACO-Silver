import datetime

'''
*  
1         2        3       4        5   6     7         8      9          10      11       12        13        14      15        16
12.7mb   12.7mb  12.7mb   12.7mb    t   t   116.3mb  585.6mb  623.7mb   624.2mb   624.4mb  624.5mb   624.4mb  630.5mb  339.3mb   t
79ms     83ms     81ms    81ms              3532ms   4832ms    4665ms   4721ms    4726ms   4677ms    4687ms   4805ms   3029ms
*
'''

N = int(input())
dst_x, dst_y = [int(x) for x in input().split()]

instructions_1 = list()
instructions_2 = list()

for i in range(N//2):
    instruction = [int(x) for x in input().split()]
    instructions_1.append(instruction)
    
for i in range(N//2, N):
    instruction = [-int(x) for x in input().split()]
    instructions_2.append(instruction)    

time1 = datetime.datetime.now()

'''
print(f'{N=}')
print(f'{instructions_1=}')
print(f'{instructions_2=}')
'''

def move_to_list(ins, new_pos_dic, old_pos, counts):
    delta_x, delta_y = ins
    x, y = old_pos
    x += delta_x
    y += delta_y
    key = (x, y)
    value = [ i+1 for i in counts]
    new_pos_dic[key] = value 
    return

def merge_dic_list(pos, pos1):
    for k, v in pos1.items():
        if k in pos:
            pos[k].extend(v)
        else:
            pos[k] = v
    return

# get all positions the robot reaches using instructions.
# be aware that each instruction can be used at most once.
# result data structure { (x,y): [cnt1, cnt2 ...]} -> to reach position (x,y),
#       there are 2 ways: way 1 needs cnt1 instructions; way 2 needs cnt2 instructions; ... 
# the issue for this data structure is test cases 5, 6, 16 times out.
# the reason is that for the above test cases, there are too many duplicated cnts.
# To reach (Xk, Yk), the results may be [1,1,1,.....1, 2,....2, ...].
# Python is not efficient looping through the list to add them together in the last step. 
# 
# using collections.Counter to store result structure has other problem. test cases [8,9,10,11,12,13,14] times out.
# the algorithm creates many Counter, which is less efficient than list.  

def move_list(instructions, start):
    x0,y0 = start
    pos = { (x0,y0): [0]}
    for ins in instructions:
        tmp_pos = dict()
        for k,v in pos.items():
            move_to_list(ins, tmp_pos, k, v)
        merge_dic_list(pos, tmp_pos)
    return pos

pos_1 = move_list(instructions_1, (0,0))
pos_2 = move_list(instructions_2, (dst_x, dst_y))
#print(f'{pos_1=}')
#print(f'{pos_2=}')
nums_ways = [0]*(1+N)
for k, v in pos_1.items():
    if k in pos_2:
        #print(f'find {k} {v} {pos_2[k]}')
        for cnt1 in v:
            for cnt2 in pos_2[k]:
                nums_ways[cnt1+cnt2]+=1
                
for i in range(1, N+1):
    print(nums_ways[i])
 
