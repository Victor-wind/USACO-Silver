''' 
All tests pass within 300 ms
'''

def check_condition_simple(N, K, M, x):
    remains = N
    days = 0
    while remains > 0:
        y = remains // x
        if y < M: y = M
        days += 1
        remains -= y
        if days > K: return False
    return True


def check_condition_optimized(N, K, M, x):
    remains = N
    days = 0
    while remains > 0:
        y = remains // x
        if y <= M: # from here, all following loan payments are M gallons, could complete the calculation. 
            days += (remains//M)
            if remains % M != 0:
                days += 1
            return days <= K
        # how many following transitions that leave y unchanged
        # for example remains: 290, X = 100, -> y = 2. It could have 45 y=2 while remains >= 200
        extra_gallons = remains - y*x
        days_followed = extra_gallons//y
        if extra_gallons % y == 0: # one more y 
            days_followed += 1
        if days_followed == 0: #  for example:  remains=202, X = 10, -> y = 20,  extra_gallons=2, days_followed=0
            days_followed = 1            
        days += days_followed
        remains -= (y * days_followed)
        if days > K: return False
    return True


with open('loan.in') as f:
    lines = f.readlines()
N, K, M = [int(x) for x in lines[0].split()]
# print(N, K, M)

# the input condition satisfies K⋅M < N -> there is a unique solution X,
# otherwise there are supper large X numbers, allow FJ to pay M gallons of milk for all days and satisfy K  < N/M
lo = 1
hi = int(N / M) + 1  # Y = N/hi -> Y < M together with K⋅M < N, so hi is larger than the answer.
# print(f'{lo=} {hi=}')
while lo <= hi:
    m = (lo + hi) // 2
    # if check_condition_simple(N, K, M, m):  # Overtime
    if check_condition_optimized(N, K, M, m):
        lo = m + 1
    else:
        hi = m - 1

print(hi)
with open('loan.out','w') as f:
    f.write(f'{hi}\n')
