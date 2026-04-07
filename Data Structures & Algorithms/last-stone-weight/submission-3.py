class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            print(first,second)
            if abs(second - first) > 0:
                heapq.heappush_max(stones, abs(second - first))

        stones.append(0)
        return stones[0]