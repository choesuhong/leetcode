class Solution:
    def intToRoman(self, num: int) -> str:
        i_to_Roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        i_to_Roman = sorted(i_to_Roman.items(), key= lambda item: -item[0])
        
        res = ''
        
        while num>0:
            for i, R in i_to_Roman:
                if num>=i:
                    res += R
                    num-=i
                    break
        
        return res