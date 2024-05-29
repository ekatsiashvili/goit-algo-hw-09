def find_min_coins(amount):
    
    coins = [50, 25, 10, 5, 2, 1]
        # Таблиця для збереження мін кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 потрібно 0 монет
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Відновлення монет (які вже використані)
    coin_count = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                if coin in coin_count:
                    coin_count[coin] += 1
                else:
                    coin_count[coin] = 1
                i -= coin
                break
    
    return coin_count

# Test
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}