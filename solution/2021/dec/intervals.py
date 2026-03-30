# only first two tests pass, others time out. The same for converted python official soultion from C++
import sys

N, M  = [ int(x) for x in sys.stdin.readline().strip().split()]

interval_dict = dict()
for _ in range(N):
    a, b = [ int(x) for x in sys.stdin.readline().strip().split()]
    interval_dict[(a,b)] = interval_dict.get((a,b), 0) + 1

a_lst = [0]*(2*M+1)
b_lst = [0]*(2*M+1)
result = [0]*(2*M+1)


interval_lst = list(interval_dict.keys())
K = len(interval_lst)

for i in range(K):
    for j in range(K):
        i_v = interval_dict[interval_lst[i]]
        j_v = interval_dict[interval_lst[j]]
        a = interval_lst[i][0] + interval_lst[j][0]
        b = interval_lst[i][1] + interval_lst[j][1]
        c = i_v*j_v
        a_lst[a] += c
        b_lst[b] += c
        
pre_sum = 0
for i in range(2*M+1):
    pre_sum += a_lst[i]
    result[i] = pre_sum
    pre_sum -= b_lst[i]

result_str = [str(x) for x in result]
print('\n'.join(result_str))
