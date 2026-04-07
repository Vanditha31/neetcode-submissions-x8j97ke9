class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        for i, t1 in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>t1:
                    stack[i] = j-i
                    break
        return stack