class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for i in range(len(s)):
            ret = max(ret, self.expand(s,i,i), self.expand(s,i,i+1), key=len)
        return ret
    def expand(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]