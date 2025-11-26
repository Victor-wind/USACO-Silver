# All tests complete within 300 ms. 

with open('swap.in') as f:
    N, M, K = map(int, f.readline().split())
    intervals = [tuple(map(int, f.readline().split())) for _ in range(M)]

# Build the permutation after applying all M reversals
cow_orders = list(range(N))
for l, r in intervals:
    cow_orders[l-1:r] = reversed(cow_orders[l-1:r])

jump_table = [-1] * N
for new_pos, old_pos in enumerate(cow_orders):
    jump_table[old_pos] = new_pos
# print(f'{jump_table=}')

# cows in a cycle must be circular, they could not be like 4->1->2->3->1...
# the reason is the jump_table's value are unique: No 2 cows could jump to the same place.
# After computing each cow's jumping sequence loop, calculate K time operation could use mod operation. 
# The time complexity below is O(N)
cow_cycle = [-1] * N # which cycle cow_i belongs to
cow_cycle_pos = [-1] * N # what is the position/index cow_i in its cycle
cycle_list = list()
for i in range(N):
    # cow index at i
    if cow_cycle[i] != -1: # already visited and assigned the cycle
        continue
    cycle_id = len(cycle_list)
    cycle = list()
    next_p = jump_table[i]
    cur_pos = i
    k = 0
    while cow_cycle[next_p] == -1:
        cow_cycle[next_p] = cycle_id
        cycle.append(next_p)
        cow_cycle_pos[cur_pos] = k
        cur_pos = next_p
        k += 1
        next_p = jump_table[next_p]
    cycle_list.append(cycle)

'''
print(f'{cow_cycle=}')
print(f'{cycle_list=}')
print(f'{cow_cycle_pos=}')
'''

final_pos = [-1] * N
for i in range(N):
    cycle_id = cow_cycle[i]
    cycle = cycle_list[cycle_id]
    pos = cow_cycle_pos[i]
    j = (pos+K-1) % (len(cycle))
    k = cycle[j]
    # print(f'{i=} {K=} {cycle_id=} {cycle=} {pos=} {j=} {k=}')
    final_pos[k] = i

with open("swap.out", "wb", buffering=8*1024*1024) as f:  # 8 MB buffer
    final_pos = [str(i+1) for i in final_pos]
    lines = "\n".join(final_pos).encode()
    f.write(lines)
