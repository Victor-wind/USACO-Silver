with open('hps.in') as f:
    lines = f.readlines()

max_win = 0
N = int(lines[0])
p_count = [0]*(N+1)
h_count = [0]*(N+1)
s_count = [0]*(N+1)

for i in range(1, N+1):
    p_count[i] =  p_count[i-1]
    h_count[i] =  h_count[i-1]
    s_count[i] =  s_count[i-1]
    if lines[i][0] == 'P': p_count[i]+=1
    if lines[i][0] == 'H': h_count[i]+=1
    if lines[i][0] == 'S': s_count[i]+=1

print(f'{p_count}')
print(f'{h_count}')
print(f'{s_count}')

for i in range(N+1):
    hps_i     = [p_count[i], h_count[i], s_count[i]]
    hps_after = [p_count[N]-p_count[i], h_count[N]-h_count[i], s_count[N]-s_count[i]]
    win_i = max(hps_i) + max(hps_after)
    max_win = max(max_win, win_i)

print(f'{max_win}')

with open('hps.out', 'w') as f:
    f.write(f'{max_win}\n')
