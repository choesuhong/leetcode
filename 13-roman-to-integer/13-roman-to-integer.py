import re

class Solution:
#     def calcul(self, Roman_dic: list, digit: int):
#         for i, R in reversed(list(enumerate(Roman_dic))):
#             if self.s.startswith(R):
#                 self.res+=i*digit
#                 self.s = self.s[len(R):]
#                 break
    
    def romanToInt(self, s: str) -> int:
#         self.s = s
#         self.res = 0
        
#         M = ['','M','MM','MMM']
#         C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
#         X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
#         I = ['','I','II','III','IV','V','VI','VII','VIII','IX']
                
#         self.calcul(M, 1000)
#         self.calcul(C, 100)
#         self.calcul(X, 10)
#         self.calcul(I, 1)
        
#         return self.res
        translations = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
    
        s = re.sub(r'IV','IIII',s)
        s = re.sub(r'IX','VIIII',s)
        s = re.sub(r'XL','XXXX',s)
        s = re.sub(r'XC','LXXXX',s)
        s = re.sub(r'CD','CCCC',s)
        s = re.sub(r'CM','DCCCC',s)
        
        res = 0
        
        for char in s:
            res += translations[char]
            
        return res