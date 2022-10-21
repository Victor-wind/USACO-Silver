import time

start = time.time()

with open('paintbarn.in') as f:
    lines = f.readlines()

N, K = [int(x) for x in lines[0].split()]
print(N, K)

corners = [[int(x) for x in line.split() ] for line in lines[1:]]
#print(corners)

areas = [ [0]*1001 for i in range(1001)]

end1 = time.time()

cnt = 0


for x in corners:
    x1, y1, x2, y2 = x[0], x[1],x[2], x[3]
    areas[x1][y1] += 1
    areas[x2][y1] -= 1
    areas[x1][y2] -= 1
    areas[x2][y2] += 1
       
for i in range(0, 1001):
    for j in range(0, 1001):
        if i > 0:
            areas[i][j] += areas[i-1][j]
        if j > 0:
            areas[i][j] += areas[i][j-1]
        if j > 0 and i > 0:
            areas[i][j] -= areas[i-1][j-1]
        if areas[i][j] == K:
            cnt += 1
                    
'''
# not the best solution. Half tests time out
print(f'elapsed time 1 {end1-start}')

for x in corners:
    x1, y1, x2, y2 = x[0], x[1],x[2], x[3], 
    for i in range(x1, x2):
        areas[i][y1] += 1
        areas[i][y2] -= 1

end2 = time.time()
print(f'elapsed time 2  {end2-start}')

for i in range(1001):
    for j in range(1001):        
        if j > 0:
            areas[i][j] += areas[i][j-1]
        if areas[i][j] == K:
            cnt += 1
'''

end3 = time.time()
print(f'elapsed time 3 {end3-start}')
print(cnt)
      
with open('paintbarn.out', 'w') as f:
    f.write(f'{cnt}\n')
