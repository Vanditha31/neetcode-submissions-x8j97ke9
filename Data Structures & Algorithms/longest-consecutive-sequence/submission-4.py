class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = []
        cnt = []
        nums = list(set(nums))
        nums.sort()
        print(nums)
        if nums == []:
            return 0
        for i, num in enumerate(nums):
            if num - 1 in seq:
                seq.append(num)
                cnt.append(len(seq))
                continue
            seq = [num]
            cnt.append(len(seq))
            print(set(nums))
            print(i, num)
            print(seq)
            print(cnt)
        return max(cnt)

