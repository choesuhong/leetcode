class Solution:
    def calcul(self, Roman_dic: list, digit: int):
        for i, R in reversed(list(enumerate(Roman_dic))):
            if self.s.startswith(R):
                self.res+=i*digit
                self.s = self.s[len(R):]
                break
    
    def romanToInt(self, s: str) -> int:
        self.s = s
        self.res = 0
        
        M = ['','M','MM','MMM']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX']
                
        self.calcul(M, 1000)
        self.calcul(C, 100)
        self.calcul(X, 10)
        self.calcul(I, 1)
        
        return self.res