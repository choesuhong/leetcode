from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        res = 0
        
        for i in s:
            if i in q:
                while i in q:
                    q.popleft()
            q.append(i)
            res = max(res, len(q))
        
        return res