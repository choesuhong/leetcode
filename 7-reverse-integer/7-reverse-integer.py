class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            res = int(''.join(str(x)[::-1]))
        else:
            res = -int(''.join(reversed(str(x)[1:])))
        return res if -2**31 <= res <= 2**31-1 else 0