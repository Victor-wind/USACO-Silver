# All tests complete within 400 ms.

# The key observation is 
# 1. Compute the result backwards by adding cows N, N-1, N-2, ... into the line. This is equivalent to removing the first 0, 1, 2, ... N-1 cows from the line.
# 2. Search which cow takes cereal k in constant time O(1) 
# 3. When cow i is added into the line, it triggers re-distribute the cereals among cows already in the line. It seems to be O(N). 
#    However, as a cow k could have either first or second cereal, it will be updated at most 2 times. Across all cows ([1,N]), the total operations take at most 2N times.  

with open('cereal.in') as f:
    N, M = [int(x) for x in f.readline().split()]
    favorites = [[int(x) for x in f.readline().split()] for _ in range(N)]
print(N,M)
# print(favorites)
cereal_assigned = [None] * (N+1)
cow_favorites = [0] * (N+1)
result = []
nums = 0


def add_cow(i):
    global nums
    cow = i
    while True:
        cow = assign_cereal(cow)
        if cow == 0:
            nums += 1
        if cow <= 0:
            result.append(nums)
            return    
    return


def assign_cereal(cow):
    first, second = favorites[cow-1] # favorites is 0 indexed, cow is 1 indexed
    first_assigned = cereal_assigned[first]
    if not first_assigned: # first favorite is not assigned, take it
        cereal_assigned[first] = cow
        return 0
    if first_assigned >= cow: # steal it from the cow whose order is less
        cereal_assigned[first] = cow
        return first_assigned # need to re-assign the cow first_assigned
    second_assigned = cereal_assigned[second]
    if not second_assigned:  # second favorite is not assigned, take it
        cereal_assigned[second] = cow
        return 0
    if second_assigned >= cow: # steal it
        cereal_assigned[second] = cow
        return second_assigned # need to re-assign the cow second_assigned
    # could not assign cereal to cow
    return -1


for i in range(N, 0, -1):
    add_cow(i)

result.reverse()
# print(result)
with open("cereal.out", "w") as f:
    s = [str(i) for i in result]
    s = '\n'.join(s)
    f.write(f'{s}\n')
