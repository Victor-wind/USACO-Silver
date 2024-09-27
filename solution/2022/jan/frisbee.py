N = int(input())
h = [int(x) for x in input().split()]

sum_dist = 0
min_stack = list()

#print(h)
for i,v in enumerate(h):
    #print(f'{i=} {v=}')
    while len(min_stack) > 0:
        j = min_stack[-1]
        x = h[j]
        #print(j+1,i+1)
        sum_dist += (i-j+1)
        if v >= x:
            min_stack.pop()            
        else:
            break
    min_stack.append(i)

print(sum_dist)
