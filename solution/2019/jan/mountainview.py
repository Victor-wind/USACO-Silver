with open('mountains.in') as f:
    lines = f.readlines()

N = int(lines[0])

mountains = [ [int(x) for x in s.split()] for s in lines[1:] ]

mountains = [ (m[0]-m[1], m[0]+m[1]) for m in mountains]
mountains.sort()

print(f'{mountains}')

most_right = (mountains[0][0]-1, mountains[0][0]-1)

mountains_cnt = 0

for m in mountains:    
    if m[1] > most_right[1]:
        mountains_cnt +=1        
        # special case: last one is covered
        if m[0] == most_right[0]:
            mountains_cnt -=1 
        most_right = m
    
        
print(f'{mountains_cnt}')       
with open('mountains.out', 'w') as f:
    f.write(f'{mountains_cnt}\n')
