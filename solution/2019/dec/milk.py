# All tests pass within 400 ms

def get_root(lst, i):
    ancestor = lst[i]
    while ancestor != lst[ancestor]:
        ancestor = lst[ancestor]
    return ancestor


with open('milkvisits.in') as f:
    lines = f.readlines()
N, M = [int(x) for x in lines[0].split()]
cow_breed = lines[1]
result_lst = ['0']* M

# to build connected components, need helper structures
root = list(range(N + 1))

for i in range(2, 2 + N - 1):
    x, y = [int(x) for x in lines[i].split()]
    # x and y are in the same connected component, if their breeds are the same.
    if cow_breed[x-1] == cow_breed[y-1]:
        root_x = get_root(root, x)
        root_y = get_root(root, y)
        root[root_y] = root_x
    # print(x, y)

# print(f'{root=}')

# if M >> N, helper to speed up finding the root: root_hash[i] returns i's root in constant time
# Not necessary in this problem
''' 
root_hash = [-1] * (N+1)
def speed_up_root(hash_lst, i, lst):
    if hash_lst[i] > 0: return hash_lst[i]
    ancestor = lst[i]
    if ancestor != lst[ancestor]:
        ancestor = speed_up_root(hash_lst, ancestor, lst)
    hash_lst[i] = ancestor
    return hash_lst[i]
for i in range(1, N+1):
    speed_up_root(root_hash, i, root)
# print(f'{root_hash=}')
'''

for i in range(2 + N - 1, 2 + N - 1 + M):
    temp_s = lines[i].split()
    a, b, c = (int(temp_s[0]), int(temp_s[1]), temp_s[2])
    # print(a, b, c)
    k = i - (2 + N - 1) # convert k to range(0,M)
    # if a, b are NOT in the same connected component, the both G and H are on the path
    # if a, b are in the same connected component, check c (G or H) is on the path
    if get_root(root, a) != get_root(root, b) or cow_breed[a-1] == c:
    # if root_hash[a] != root_hash[b] or cow_breed[a - 1] == c:
        result_lst[k] = '1'

result = ''.join(result_lst)
print(result)
with open('milkvisits.out', 'w') as f:
    f.write(f'{result}\n')
