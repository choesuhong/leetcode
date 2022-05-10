class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        s = s.strip()
        
        if s == '':
            return 0
        
        sign = -1 if s[0]=='-' else 1
        if s[0] in ['+','-']:
            s = s[1:]
        
        i = 0
        while i < len(s) and s[i].isdigit():
            res = 10*res + int(s[i])
            i+=1
        
        res = sign*res
        if res>2**31-1: res = 2**31-1
        elif res<-2**31: res = -2**31
        
        return res