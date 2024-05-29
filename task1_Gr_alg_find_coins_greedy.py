def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count[coin] = count
            amount -= coin*count
    
    return coin_count
# Test
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}