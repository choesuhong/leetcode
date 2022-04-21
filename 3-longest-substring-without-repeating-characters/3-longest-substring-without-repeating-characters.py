class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        res, start = 0, 0
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                res = max(res, i - start + 1)
                
            usedChar[s[i]] = i
        return res