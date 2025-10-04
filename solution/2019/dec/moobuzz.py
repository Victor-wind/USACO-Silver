with open('moobuzz.in') as f:
    lines = f.readlines()

N = int(lines[0])
result = -1


def get_numbers(k):
    # return the numerical numbers within position [1,K] excluding fizz, buzz, fizzbuzz
    if k <= 0: return 0
    fizz_cnt = k//3
    buzz_cnt = k//5
    fizzbuzz_cnt = k//15
    return k - fizz_cnt - buzz_cnt + fizzbuzz_cnt

# The official solution is fine, but the binary search is more intuitive
# Within position [1,i], there is a responding numerical number j excluding fizz, buzz, fizzbuzz
# The goal is to find the smallest position i, whose number is N
low_pos = 1
high_pos = 1_000_000_000_00 # Overestimate upper bound
while low_pos < high_pos:
    mid_pos = (low_pos+high_pos)//2
    j = get_numbers(mid_pos)
    if j < N:
        low_pos = mid_pos + 1
    else:
        high_pos = mid_pos
    # print(low_pos, high_pos)

result = low_pos
print(result)
with open('moobuzz.out', 'w') as f:
    f.write(f'{result}\n')
