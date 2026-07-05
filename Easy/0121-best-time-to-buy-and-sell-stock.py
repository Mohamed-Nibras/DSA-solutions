class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        profit = 0
        smallest = prices[0]
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            else:
                profit = prices[i] - smallest
                if profit > max_profit:
                    max_profit = profit

        return max_profit
    
a = Solution()
print(a.maxProfit([7,6,4,3,1]))