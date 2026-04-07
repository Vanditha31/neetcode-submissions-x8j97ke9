class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p: list) -> float:
            return ((p[0]**2) + p[1]**2)**(1/2)

        d = []
        heapq.heapify_max(d)

        for p in points:
            heapq.heappush_max(d, [distance(p)] + p)
            if len(d) > k:
                heapq.heappop_max(d)

        res = []
        while d:
            dist, x, y = heapq.heappop_max(d)
            res.append([x,y])

        return res
        