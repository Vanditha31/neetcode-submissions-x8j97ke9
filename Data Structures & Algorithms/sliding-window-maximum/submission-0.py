class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        max_nums = []
        while r <= len(nums):
            max_nums.append(max(nums[l:r]))
            l += 1
            r += 1
        return max_nums
