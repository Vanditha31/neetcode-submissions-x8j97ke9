class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            print(f"{res}", f"{num}")
            res = num ^ res
            print(res)
        return res