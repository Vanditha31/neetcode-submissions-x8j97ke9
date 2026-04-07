class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        print(stack)
        for i, t1 in enumerate(temperatures):
            print(i, t1)
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>t1:
                    stack[i] = j-i
                    print(stack)
                    break
        return stack