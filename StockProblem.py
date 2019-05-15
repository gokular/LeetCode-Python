# Given an list for which the ith element is the price of a given stock on day i, find the maximum profit
# when buying and selling one stock on two days

class Solution:
    def maxProfit(prices) -> int:
        profit = 0
        max = 0
        diff = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[i] < prices[j]):
                    diff = prices[j]-prices[i]
                    if(max < diff):
                        max = diff
            if(profit < max):
                profit = max
        return profit

    price = [7,6,4,3,8]
    print(maxProfit(price))
