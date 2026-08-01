class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(s)
        b=sorted(t)
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)