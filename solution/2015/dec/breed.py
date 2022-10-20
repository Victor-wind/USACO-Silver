with open('bcount.in') as f:
    lines = f.readlines()

N, Q = [int(x) for x in lines[0].split()]
print(N, Q)

cows = [ int(lines[i]) for i in range(1, N+1)]
print(cows)

queries = [ [ int(x) for x in lines[i].split()] for i in range(N+1, N+1+Q)]
print(queries)

Holsteins = [0] * (N+1)
Guernseys = [0] * (N+1)
Jerseys   = [0] * (N+1)

for i, cow in enumerate(cows):
    Holsteins[i+1] = Holsteins[i]
    Guernseys[i+1] = Guernseys[i]
    Jerseys[i+1]   = Jerseys[i]
    if cow == 1: Holsteins[i+1] += 1
    if cow == 2: Guernseys[i+1] += 1
    if cow == 3: Jerseys[i+1] += 1

print(Holsteins)
print(Guernseys)
print(Jerseys)
        
with open('bcount.out', 'w') as f:
    for query in queries:
        s, e = query
        h = Holsteins[e]-Holsteins[s-1]
        g = Guernseys[e]-Guernseys[s-1]
        j = Jerseys[e]-Jerseys[s-1]
        f.write(f'{h} {g} {j}\n')
