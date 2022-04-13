from collections import deque
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [n*[0] for i in range(n)]
        
        dy = deque([0, 1, 0, -1])
        dx = deque([1, 0, -1, 0])
        
        y, x = 0, 0
        
        for i in range(1, n**2+1):
            try:
                if m[y + dy[0]][x + dx[0]] != 0:
                    raise ValueError
            except:
                dy.rotate(-1)
                dx.rotate(-1)
                
            m[y][x] = i
            y += dy[0]
            x += dx[0]
             
        return m