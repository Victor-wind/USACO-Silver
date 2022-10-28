with open('rental.in') as f:
    lines = f.readlines()
N, M, R = [int(x) for x in lines[0].split()]
print(f'{N} {M} {R}')

milks = [int(lines[i]) for i in range(1, N+1)]
milks.sort(reverse=True)
print(f'{milks}')

milks_to_sell = [ [int(x) for x in lines[i].split()]for i in range(N+1, N+M+1)]
milks_to_sell.sort(key=lambda x: x[1], reverse=True)
print(f'{milks_to_sell}')

rental = [int(lines[i]) for i in range(N+M+1, N+M+R+1)]
rental.sort(reverse=True)
print(f'{rental}')

max_profit = 0

shop_index = 0
def milk2money_update(milk):
    global shop_index
    if milk <= 0: return 0
    if shop_index >= len(milks_to_sell): return 0
    profit = 0
    while milk > 0:
        to_buy = min(milk, milks_to_sell[shop_index][0])
        profit += to_buy*milks_to_sell[shop_index][1]
        milks_to_sell[shop_index][0] -= to_buy
        milk -= to_buy
        if milks_to_sell[shop_index][0] == 0:
            shop_index += 1
        if shop_index == len(milks_to_sell):
            milk = 0
    return profit

def milk2money(milk):
    global shop_index
    i = shop_index
    if milk <= 0: return 0
    if i >= len(milks_to_sell): return 0
    profit = 0
    while milk > 0:
        to_buy = min(milk, milks_to_sell[i][0])
        profit += to_buy*milks_to_sell[i][1]
        milk -= to_buy
        if milks_to_sell[i][0] == to_buy:
            i += 1
        if i == len(milks_to_sell):
            milk = 0
    return profit

cow_index  = 0
rent_index = 0
for i in range(N):
    # for cow_index, if keep it for milk,   
    profit_milk = milk2money(milks[cow_index])
    # if rent it
    profit_rent = rental[rent_index] if rent_index < R else 0

    if profit_milk == 0 and profit_rent == 0:
        break
    # keep it for milk
    if profit_milk >= profit_rent:
        max_profit += profit_milk
        # update internal structure
        milk2money_update(milks[cow_index])
        cow_index += 1
    else:
        max_profit += profit_rent
        # don't change cow_index, as only rent the cow producing least milk
        rent_index += 1        
    
print(f'{max_profit}')       
with open('rental.out', 'w') as f:
    f.write(f'{max_profit}\n')
