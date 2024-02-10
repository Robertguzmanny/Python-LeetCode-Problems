class Solution:
    def maxProfit(self, prices):
        minPrice = float("inf")
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price 
            elif price - minPrice > maxProfit: 
                maxProfit = price - minPrice

        return maxProfit
    
test = Solution()

arr = [7, 6, 5, 1, 3, 2]
print(test.maxProfit(arr))