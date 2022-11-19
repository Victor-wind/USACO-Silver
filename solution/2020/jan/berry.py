
with open('berries.in') as f:
    lines = f.readlines()

N, K = [int(x) for x in lines[0].split()]
print(N, K)

berries = [int(x) for x in lines[1].split()]
berries.sort(reverse=True)
#print(berries)

max_cnt = 0
basket_size = 0

#iterate all possible basket size, find the best combination. 
for basket_size in range(1, berries[0]+1):
    temp_list = []
    cnt = 0
    for berry in berries:
        while berry >= basket_size:
            temp_list.append(basket_size)
            berry -= basket_size
            cnt += 1
            # optimize the code: if already found full K basket, stop
            if cnt >= K: break         

        # optimize the code: if already found full K basket, stop
        if cnt >= K:
            break

        if berry > 0:
            temp_list.append(berry)
            
    temp_list.sort(reverse=True)
    
    # Elsie keeps the largest [0, K/2) baskets,
    # Bessie keeps [K//2, K) baskets
    berry_basket = temp_list[K//2:K]
    max_cnt = max(max_cnt, sum(berry_basket))
    # print(f'{berry_basket=}')
    # print(temp_list, cnt, K)

print(max_cnt)
with open('berries.out','w') as f:
    f.write(f'{max_cnt}\n')
