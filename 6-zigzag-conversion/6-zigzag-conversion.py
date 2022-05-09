class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = numRows*['']
        zigzag[0] = s[0]
        row, direction = 0, 1
        
        for i in range(1,len(s)):
            d_row = row+direction
            if not 0<= d_row < numRows:
                direction = -direction
                d_row = row+direction
            row = d_row
            zigzag[row] += s[i]
        
        return ''.join(zigzag)