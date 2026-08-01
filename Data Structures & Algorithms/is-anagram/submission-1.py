class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(s)
        b=sorted(t)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if a[i]!=b[i]:
                return False
        return True