from itertools import permutations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dic = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        if not digits:
            return []
        
        res = digits_dic[digits[0]]
        
        for i in range(1,len(digits)):
            new_res = []
            for s1 in res:
                for s2 in digits_dic[digits[i]]:
                    new_res.append(s1+s2)
            res = new_res
        
        return res