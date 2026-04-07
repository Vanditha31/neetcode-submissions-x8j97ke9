class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.s:
            self.s[key] = []
        if [value, timestamp] not in self.s[key]:
            self.s[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.s[key]) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if self.s[key][m][1] <= timestamp:
                res = self.s[key][m][0]
                l = m + 1
            else:
                r = m - 1

        return res
