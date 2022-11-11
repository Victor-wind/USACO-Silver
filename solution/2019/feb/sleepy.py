with open('herding.in') as f:
    lines = f.readlines()

N = int(lines[0])
cows = [int(x) for x in lines[1:]]
cows.sort()
#print(f'{cows}')
min_moves = 0

# move a windows (size N) from the first cow to the last cow.
# Cows outside of the window are "endpoints". Move them into the window to fill the empty slots.
# The window with the least empty slots needs minimal moves.
# Exceptions: N-1 cows are in continuous positions, need to move 2, not 1. 
max_cows_in_window = 0
cnt = 0
j = 0
for i in range(N):
        while j < N and (cows[j]-cows[i]+1) <= N:
                j += 1                
        max_cows_in_window = max(max_cows_in_window, j-i)
        #print(f'{i=} {j=} {max_cows_in_window=}')     

#print(f'{max_cows_in_window=}')
min_moves = N-max_cows_in_window

if cows[N-2]-cows[0]== N-2 and cows[N-1]-cows[N-2] > 2:
        min_moves =2
if cows[N-1]-cows[1]== N-2 and cows[1]-cows[0] > 2:
        min_moves =2
        
print(min_moves)


# each move from "endpoint" will remove the empty slots on the ends.
# for the max moves, compare both empty slots on the ends,
# move from the smaller end to fill the larger end
# AoooBoCoooDooX
# on left, 3 empty slots between A and B, on right, 2 empty slots between D and X
# move x to left to fill the 3 empty slots by switch A, X.
# AXooBoCoooD -> XAoBoCoooD -> AXBoCoooD
# After that, all slots can be filled by swtching the endpoints. 

max_moves = max(cows[N-2]-cows[0], cows[N-1]-cows[1]) - (N-2)
        
print(max_moves)
with open('herding.out','w') as f:
    f.write(f'{min_moves}\n')
    f.write(f'{max_moves}\n')
       
