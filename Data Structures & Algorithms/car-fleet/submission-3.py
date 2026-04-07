class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        for i, p in enumerate(position):
            time[i] = (target - p)/speed[i]
        pos_t_zip = zip(position,time)
        pos_t = list(pos_t_zip)
        pos_t.sort(reverse=True)
        print(pos_t)
        stack = []
        fleet = 1
        for i,j in pos_t:
            if stack and j > stack[-1]:
                fleet += 1
            elif stack and j <= stack[-1]:
                j = stack[-1]
            stack.append(j)
        return fleet