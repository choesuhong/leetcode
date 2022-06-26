class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(min(strs,key=len))
        res = ''
        
        for i in range(length):
            tmp = strs[0][i]
            if not all(map(lambda x: x[i]==tmp, strs)):
                break
            res += tmp
            
        return res