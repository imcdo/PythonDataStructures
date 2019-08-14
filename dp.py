def coin_change(coins, target):
    cache = [0]
    for i in range(1, target + 1):
        choices = []

        for den in coins:
            if i-den >= 0 and cache[i-den] is not None: 
                choices.append(cache[i-den] + 1)
        
        if len(choices) == 0:
            cache.append(None)
        else:
            cache.append(min(choices))
    return cache


print(str(coin_change((3, 9, 17), 100)))
