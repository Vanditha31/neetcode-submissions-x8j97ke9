class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2

            rate = [-(i//-m) for i in piles]
            if sum(rate) <= h:
                r = m - 1
                res = m
            elif sum(rate) > h:
                l = m + 1

        return res


            