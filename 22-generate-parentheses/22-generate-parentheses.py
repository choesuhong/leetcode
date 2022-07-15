class Solution:
    def generate(self, left, right, res, s, n):
        if len(s) == n*2:
            res.append(s)
            return
        
        if left < n:
            self.generate(left+1, right, res, s+'(', n)
        if right < left:
            self.generate(left, right+1, res, s+')', n)
        
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(0,0,res,'',n)
        
        return res