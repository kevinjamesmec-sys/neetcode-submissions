class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        r = ""

        for i in s:
            if i.isalnum():
                i = i.lower()
                p += i
                r = i + r

        return p == r