from collections import Counter
import datetime

N = int(input())
dst_x, dst_y = [int(x) for x in input().split()]

instructions_1 = list()
instructions_2 = list()
instructions = list()

for i in range(N):
    instruction = [int(x) for x in input().split()]
    instructions.append(instruction)

#print(f'{instructions=}')

instructions_1 = instructions[0:N//2]
instructions_2 = instructions[N//2:]
instructions_2 = [ [-x[0], -x[1]] for x in instructions_2]

'''
print(f'{N=}')
print(f'{len(instructions_1)} {instructions_1=}')
print(f'{len(instructions_2)} {instructions_2=}')
'''
time1 = datetime.datetime.now()

def move_to_counter(ins, new_pos_dic, old_pos, counter):
    delta_x, delta_y = ins
    x, y = old_pos
    x += delta_x
    y += delta_y
    key = (x, y)
    value = Counter({(key+1): value for key, value in counter.items()})    
    new_pos_dic[key] = value 
    return

def merge_dic_counter(pos, pos1):
    
    for k, v in pos1.items():
        if k in pos:
            pos[k] = pos[k]+v
        else:
            pos[k] = v
    return
# get all positions the robot reaches using instructions.
# be aware that each instruction can be used at most once.
# result { (x,y): [cnt1, cnt2]} -> to reach position (x,y),
#       there are 2 ways: way 1 needs cnt1 instructions; way 2 needs cnt2 instructions;
def move_counter(instructions, start):
    x0,y0 = start
    pos = { (x0,y0): Counter({0:1})}
    for ins in instructions:
        tmp_pos = dict()
        for k,v in pos.items():
            move_to_counter(ins, tmp_pos, k, v)
        merge_dic_counter(pos, tmp_pos)
    return pos

pos_1 = move_counter(instructions_1, (0,0))
pos_2 = move_counter(instructions_2, (dst_x, dst_y))
#print(f'{pos_1=}')
#print(f'{pos_2=}')
time2 = datetime.datetime.now()
#print("elapsed time 1 is: ", time2-time1)

nums_ways = [0]*(1+N)
for pos, counter in pos_1.items():
    if pos in pos_2:
        #print(f'find {pos} {counter} {pos_2[pos]}')
        for ins1, cnt1 in counter.items():
            for ins2, cnt2 in pos_2[pos].items():
                nums_ways[ins1+ins2]+=(cnt1*cnt2)
                
for i in range(1, N+1):
    print(nums_ways[i])

