with open('pairup.in') as f:
    lines = f.readlines()

N = int(lines[0])
M = 0
time_list = list()

for i in range(N):
    line = lines[i+1]
    x, y = [int(x) for x in line.split()]
    #print(x, y)
    time_list.append([y,x])
    M += x

time_list.sort()
#print(f'{time_list}')   

left, right = 0, len(time_list)-1
min_time = time_list[0][0]+time_list[-1][0]

while left < right:
    amount_time = time_list[left][0]+time_list[right][0]
    min_time = max(min_time, amount_time)
    
    move = min(time_list[left][1], time_list[right][1])
    time_list[left][1] -= move    
    if time_list[left][1] == 0:
        left += 1
    time_list[right][1] -= move
    if time_list[right][1] == 0:
        right -= 1
     

print(f'{min_time}')       
with open('pairup.out', 'w') as f:
    f.write(f'{min_time}\n')
