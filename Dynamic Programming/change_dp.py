def get_change(money):
    coin_value_list=[1,3,4]
    min_coins_needed=[0]*(money+1)
    last_coin_used = [0]*(money+1)
    for i in range(money+1):
        money_value = i
        coin_value = 1
        for j in [coin for coin in coin_value_list if coin <= i]:
            if min_coins_needed[i-j]+1 < money_value:
                money_value = min_coins_needed[i-j]+1
                coin_value = j
        min_coins_needed[i] = money_value
        last_coin_used[i] = coin_value
    return min_coins_needed[money]

print(get_change(5))
