class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        for i, a in enumerate(s):
            if s[i] == s[len(s) - i - 1]:
                continue
            else:
                return False
        return True
