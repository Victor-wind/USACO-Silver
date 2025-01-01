T = int(input())

def guess_cost(marbles, guess):
    even_play = marbles[0]
    odd_play  = marbles[1]
    cost = 0    
    # Elsie guessing even
    if guess == 0:
        cost = odd_play[-1] if odd_play else -even_play[0]            
    # Elsie guessing odd
    else:
        cost = even_play[-1] if even_play else -odd_play[0]
    #print(f'  guess_cost: {guess=} {marbles=} {cost=} {even_play=} {odd_play=}')
    return cost        
    
# Binary search takes O(2^M), too slow to pass tests
# Take advantage of dynamic programming concept. From the last round, reversely calculate
# how many marbles Elsie should at least have if guessing Even or Any (Even or Odd)
# Then from round 1,2,3 ... M, based on even_marbles and min_marbles at each round,
# guess Even (if possible) or Odd, and reduce the marbles_avail from the worst scenario.
def solve(N, M, marbles):
    # min number of marbles Elsie at least should have for not losing at each turn
    min_marbles = [1]*(M+1)
    # if guessing even, min number of marbles Elsie at least should have for not losing at each turn 
    even_marbles = [1]*(M+1)
    for i in reversed(range(M)):        
        needed = odd_marbles = min_marbles[i+1]
        cost_even = guess_cost(marbles[i],0)
        even_marbles[i] = max(needed+cost_even, 1)
        cost_odd = guess_cost(marbles[i],1)
        odd_marbles = max( (needed+cost_odd), 1)
        min_marbles[i] = min(odd_marbles, even_marbles[i])        

    #print(f'{min_marbles=} {even_marbles=}')
    # start with N marbles, make decision each turn/round: could guess even?; if not, guess odd? 
    marbles_avail = N
    if marbles_avail < min_marbles[0]:
        print(-1)
        return
    for i in range(M):        
        if marbles_avail < min_marbles[i]:
            print('Made a mistake!')
            return
        if marbles_avail >= even_marbles[i]:
            print('Even', end='\n' if i == M-1 else ' ')
            cost_even = guess_cost(marbles[i],0)
            marbles_avail -= cost_even
        else:
            print('Odd', end='\n' if i == M-1 else ' ')
            cost_odd = guess_cost(marbles[i],1)
            marbles_avail -= cost_odd            
    return

for _ in range(T):
    N,M,K = [int(i) for i in input().split()]
    #print(f'{N=} {M=} {K=}')
    marbles = list()
    for _ in range(M):
        round_i = [int(i) for i in input().split()]
        even_marbles = sorted([j for j in round_i if j % 2 == 0])
        odd_marbles = sorted([j for j in round_i if j % 2 != 0])
        marbles.append([even_marbles, odd_marbles])
    #print(marbles)
    solve(N, M, marbles)
