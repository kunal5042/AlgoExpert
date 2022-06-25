def nonConstructibleChange(coins):
    Change  = 0
    coins.sort()

    for coin in coins:
        if coin > Change + 1:
            return Change + 1
        else:
            Change += coin

    return Change + 1

'''
O(nlogn) time | O(1) space - where n is the number of coins
'''

# Kunal Wadhwa
