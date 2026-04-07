class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        elif len(s1) == len(s2):
            return sorted(s1) == sorted(s2)
        else:
            l = 0
            for r in range(len(s1), len(s2) + 1):
                print(s2[l:r])
                if sorted(s1) == sorted(s2[l:r]):
                    return True
                else:
                    l += 1
                    print(l)
        return False
        