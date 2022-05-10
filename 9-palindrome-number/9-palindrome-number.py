class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s = str(x)
        l,r = 0, len(s)-1
        
        while l<=r and s[l]==s[r]:
            l+=1
            r-=1
            
        return False if l<r else True