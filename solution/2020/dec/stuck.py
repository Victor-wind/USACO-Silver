# all tests pass within 100 ms

list_east = []
list_north = []


N = int(input())
#print(N)

# each cow in format [x, y, stopped, blames (default 0), index]
for i in range(N):
    cow = input().split()
    if cow[0] == 'E':
        list_east.append( [int(cow[1]), int(cow[2]), 0, 0, i])
    else:
        list_north.append([int(cow[1]), int(cow[2]), 0, 0, i])

list_north.sort()
list_east.sort(key = lambda x: x[1])
#print(f'{list_east}')
#print(f'{list_north}')

for i in range(len(list_east)):
    east = list_east[i]
    if east[2] == 1: # cow is already stopped  
        continue
    for j in range(len(list_north)):
        north = list_north[j]
        if north[2] == 1: # cow is already stopped
            continue
        if east[0] > north[0] or east[1] < north[1]: # will not intersect
            continue
        # may intersect
        x, y = north[0]-east[0], east[1]-north[1]
        if x < y: # east stops north
            north[2] = 1
            east[3] += north[3]+1            
        if y < x: # north stops east
            east[2] = 1
            north[3] += east[3]+1
            break

list_all = list_east + list_north
list_all.sort(key = lambda x: x[4])

# print(f'{list_all}')

for x in list_all:
    print(x[3])
