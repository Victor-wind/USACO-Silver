# All tests pass within 1500 MS

s = input().strip()
t = input().strip()
Q = int(input())

def process_query(query):
    n = len(query)
    if n == 1:
        return status[query]    
    for i in range(n-1):
        for j in range(i+1, n):
            x = query[i]
            y = query[j]
            if not status[(x,y)]:
                return False
    return True

letters = 'abcdefghijklmnopqr'
N = len(letters)

status = dict()
for i in range(N):
    for j in range(i, N):
        x = letters[i]
        y = letters[j]
        compare_result = False
        if x == y:
            if s.count(x) == t.count(x): 
                compare_result = True
            status[(x)] = compare_result
        else:
            k_set = set((x,y))
            s_filtered = filter(k_set.__contains__, s)
            t_filtered = filter(k_set.__contains__, t)
            s_str = "".join(s_filtered)
            t_str = "".join(t_filtered)
            if s_str == t_str:
                compare_result = True
            status[(x, y)] = compare_result


results = list()
for _ in range(Q):
    query = input().strip()
    results.append(process_query(query))

results_str = ''.join(['Y' if x else 'N' for x in results])
print(results_str)
