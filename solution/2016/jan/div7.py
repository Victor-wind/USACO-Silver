with open('div7.in') as f:
    lines = f.readlines()

N = int(lines[0])

ids = [ int(i) for i in lines]
# print(f'{ids}')

mod_index = [None] * 7
mod_index[0] = 0

ids_sum = 0
max_cnt = 0

for i, v in enumerate(ids):
    # print(i,v)
    if i == 0: continue    
    ids_sum  += v
    mod = ids_sum % 7
    if mod_index[mod] is None:
        mod_index[mod] = i
    else:
        max_cnt = max(max_cnt, i - mod_index[mod])

print(f'{max_cnt}')

with open('div7.out', 'w') as f:
    f.write(f'{max_cnt}\n')
