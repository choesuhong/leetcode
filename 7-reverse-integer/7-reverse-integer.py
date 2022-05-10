class Solution:
    def reverse(self, x: int) -> int:
        signed = [1, -1][x<0]
        res = signed*int(str(abs(x))[::-1])
        return res if -2**31<= res <= 2**31-1 else 0