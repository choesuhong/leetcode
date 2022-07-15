from collections import Counter
class Solution:
    def plus_parentheses(self, s: str, n: int):
        C = Counter(s)
        new_s = []
        if C['('] > C[')']:
            new_s.append(s + ')')
        if C['('] < n:
            new_s.append(s + '(')
        return new_s
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['(']
        
        for i in range(n*2-1):
            tmp = []
            for r in res:
                tmp += self.plus_parentheses(r, n)
            res = tmp
            
        return res
        
        