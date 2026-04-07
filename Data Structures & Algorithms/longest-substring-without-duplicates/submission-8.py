class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        counter = 0
        stack = []
        for i, sub in enumerate(s):
            if stack and sub in stack:
                maxL = max(maxL, len(stack))
                stack = stack[stack.index(sub) + 1:]
                stack.append(sub)
                counter = len(stack)
            else:
                stack.append(sub)
                counter += 1
                maxL = max(maxL, counter)
        return maxL
