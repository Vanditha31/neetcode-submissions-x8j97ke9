class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        math = ['+', '-', '*', '/']
        if len(tokens) == 1:
            return int(*tokens)
        for n, t in enumerate(tokens):
            if t in math:
                if t == '+':
                    res = stack[-2] + stack[-1]
                elif t == '-':
                    res = stack[-2] - stack[-1]
                elif t == '*':
                    res = stack[-2] * stack[-1]
                else:
                    res = int(stack[-2] / stack[-1])
                if n == len(tokens)-1:
                    return res
                print(stack)
                stack.pop()
                stack.pop()
                stack.append(res)
                print(stack)
                res = []
            else:
                stack.append(int(t))
