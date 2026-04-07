class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {']': '[', '}': '{', ')': '('}
        stack = []
        if s[0] in bracket.keys():
            return False
        for i, b in enumerate(s):
            if b in bracket.values():
                stack.append(b)
            if b in bracket.keys() and len(stack) > 0:
                if stack[-1] == bracket[b]:
                    stack.pop()
                    if stack == [] and i == len(s) - 1:
                        return True
                    continue
                return False
        return False
                

