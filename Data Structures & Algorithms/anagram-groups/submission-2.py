class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = {}
        for i, word in enumerate(strs):
            strs_sorted[i] = "".join(sorted(word))
        
        value_to_keys = defaultdict(list)
        for k, v in strs_sorted.items():
            value_to_keys[v].append(k)

        l = []
        for k, v in value_to_keys.items():
            l1 = []
            for i in value_to_keys[k]:
                l1.append(strs[i])
            l.append(l1)

        return l