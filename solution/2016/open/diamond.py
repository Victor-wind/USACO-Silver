with open('diamond.in') as f:
    lines = f.readlines()

N, K = [int(x) for x in lines[0].split()]

print(N,K)

diamonds = [ int(x) for x in lines[1:]]

diamonds.sort()

#print(diamonds)
max_cnt = 1

'''
# Only pass half tests

# find the max count of diamonds, the smallest Must be ith diamond. 
def count_at(diamonds, N, K, i):
   cnt = 0
   j = i
   while j < N:
      if diamonds[j] > diamonds[i]+K:
         break
      j += 1
      cnt += 1
   return cnt, j

# find the max count of diamonds, the smallest could be ith diamond or after. 
# sliding window: complexity O(n)
def count_since(diamonds, N, K, i):
   max_cnt = 0
   j = i
   while j < N:
      if diamonds[j] <= diamonds[i]+K:
         max_cnt = max(max_cnt, j-i+1)
         j +=1
      else:
         while diamonds[j] > diamonds[i]+K:
            i += 1
   return max_cnt

for i in range(N):
   cnt1, j = count_at(diamonds, N, K, i)
   cnt2 = count_since(diamonds, N, K, j)
   max_cnt = max(max_cnt, cnt1+cnt2)
'''

mx = [0] * N # max count of diamonds, i must be the smallest one.
j = 0
for i in range(N):
   while j < N and diamonds[j] <= diamonds[i]+K:
      j+=1
   j -=1
   mx[i] = j-i+1

# max count of diamonds since ith diamonds, i may or may Not be the smallest one.
smx = [0] * (N+1)
smx[N-1] = mx[N-1]
for i in range(N-2,-1, -1):
   smx[i] = max(mx[i], smx[i+1])

# two boxes: the first box must start with ith diamond,
# the second box holds most possile diamonds, the smallest one's index >= (mx[i]+i)
for i in range(N-1): # skip the last one to avoid index out of range error
   max_cnt = max(max_cnt, mx[i]+smx[i+mx[i]])

print(max_cnt)
with open('diamond.out','w') as f:
    f.write(f'{max_cnt}\n')   
