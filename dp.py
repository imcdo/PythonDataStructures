def coin_change(coins, target):
    cache = [0]
    for i in range(1, target + 1):
        choices = []

        for coin in coins:
            if i-coin >= 0 and cache[i-coin] is not None: 
                choices.append(cache[i-coin] + 1)
        
        if len(choices) == 0:
            cache.append(None)
        else:
            cache.append(min(choices))
    return cache


print(str(coin_change((3, 9, 17), 100)))
 