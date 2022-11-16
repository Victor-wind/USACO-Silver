with open('lemonade.in') as f:
    lines = f.readlines()

N = int(lines[0])
arrives = [ int(x) for x in lines[1].split()]
arrives.sort(reverse = True)
# print(f'{arrives=}')

cnt = 0
for x in arrives:
    if x < cnt:
        break
    cnt += 1

print(cnt)            
with open('lemonade.out','w') as f:
    f.write(f'{cnt}\n')
    
    
