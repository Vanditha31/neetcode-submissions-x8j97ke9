class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]
        suffix_max = []

        for i, h in enumerate(height):
            if i > 0:
                prefix_max.append(max(height[:i]))
            if i < len(height) - 1:
                suffix_max.append(max(height[i+1:]))
        suffix_max.append(0)
        
        area = []
        for i, h in enumerate(height):
            a = min(prefix_max[i], suffix_max[i]) - h
            if a >= 0:
                area.append(a)
        return sum(area)

