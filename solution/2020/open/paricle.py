# All tests pass within 400 ms

with open('moop.in') as f:
    N = int(f.readline())
    particles = [ [int(x) for x in f.readline().split()] for _ in range(N)]

particles.sort()
print(N)
#print(particles)
components = list()

# index i is component's id,
# components[i] stores the smallest y of all particles in component i
components.append(particles[0][-1])
last_id = 0 
for i in range(1, N):
    y = particles[i][1]
    last_id = len(components)
    # add particles[i] as a single particle component 
    components.append(y)
    # could it combine with previous components?
    # print(f'Debug {i=} {y=} {components[-2]=}')
    while len(components) > 1 and y >= components[-2]:
        components[-2] = min(components[-1],components[-2]) 
        components.pop()
        last_id = len(components)-2
        
result = len(components)
print(result)
with open('moop.out', 'w') as f:
    f.write(f'{result}\n')
