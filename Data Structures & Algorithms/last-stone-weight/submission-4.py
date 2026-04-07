class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if abs(second - first) > 0:
                heapq.heappush_max(stones, abs(second - first))

        stones.append(0)
        return stones[0]