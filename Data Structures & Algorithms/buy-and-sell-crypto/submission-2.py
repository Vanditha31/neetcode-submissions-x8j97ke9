class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]

        for i, p in enumerate(prices):
            if prices[i+1:]:
                if p < max(prices[i+1:]):
                    profits.append(max(prices[i+1:]) - p)
            else:
                continue

        return max(profits)