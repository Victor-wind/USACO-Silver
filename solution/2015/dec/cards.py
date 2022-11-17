
with open('highcard.in') as f:
    lines = f.readlines()

N = int(lines[0])
cards = [0] * (2*N+1)
for x in lines[1:]:
    cards[int(x)] = 1

Bessie_cards = [0]*(N+1)
Elsie_cards  = [0]*(N+1)

i, j = 1, 1
for k in range(1, 2*N+1):
    if cards[k] == 1:
        Elsie_cards[i] = k
        i += 1
    else:
        Bessie_cards[j] = k
        j += 1

#print(f'{Elsie_cards=}')
#print(f'{Bessie_cards=}')

win_cnt = 0
j = 1

for i in range(1, N+1):
    while j < N+1 and Elsie_cards[i] > Bessie_cards[j]:
        j += 1
    if j == N+1:
        break
    j += 1
    win_cnt+= 1

print(win_cnt)            
with open('highcard.out','w') as f:
    f.write(f'{win_cnt}\n')
  
 
