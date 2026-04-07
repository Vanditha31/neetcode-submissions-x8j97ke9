class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        counter = 0

        while l < r:
            if nums[l] > nums[r]:
                counter += 1
                l += 1
            else:
                break
            
        return nums[counter]