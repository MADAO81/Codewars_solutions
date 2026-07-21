# https://www.codewars.com/kata/541af676b589989aed0009e7/train/python

# def count_change(money, coins):
#     if money<0:
#         return 0
#     if money == 0:
#         return 1
#     if money>0 and not coins:
#         return 0
#     return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])
  

def count_change(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]
    return dp[money]
