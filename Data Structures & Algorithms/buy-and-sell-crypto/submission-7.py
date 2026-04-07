class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = [0]

        # for i, p in enumerate(prices):
        #     if prices[i+1:]:
        #         if p < max(prices[i+1:]):
        #             profits.append(max(prices[i+1:]) - p)
        #     else:
        #         continue

        # return max(profits)
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r]-prices[l])
            r+=1
        return max_profit