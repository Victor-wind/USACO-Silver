signals = []

with open('maxcross.in') as f:
    lines = f.readlines()

#print(f'{lines=}')

N, K, B = [int(x) for x in lines[0].split()]

#print(f'{N=} {K=} {B=}' )

crosses = [0] * (N+1)
sum_sig = [0] * (N+1)

for i in range(1, B+1):
    signals.append(int(lines[i]))

for v in signals:
    crosses[v] = 1

for i in range(1, N+1):
    sum_sig[i] = sum_sig[i-1] + crosses[i]

#print(f'{sum_sig=}')
#print(f'{crosses=}')

min_repair = N+1

for i in range(K, N+1):
    repair = sum_sig[i] - sum_sig[i-K]
    min_repair = min(min_repair, repair)

with open('maxcross.out', 'w') as f:
    f.write(f'{min_repair}\n')
