# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         N = len(nums)
#         if N==3:
#             return sum(nums)
        
#         nums.sort()
#         res = 100000
        
#         for i in range(N-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
                
#             l, r = i+1, N-1
            
#             while l<r:
#                 tsum = sum([nums[i],nums[l],nums[r]])
                
#                 if tsum==target:
#                     return tsum
                
#                 if abs(tsum-target) < abs(res-target):
#                     res = tsum
                    
#                 if tsum<target:
#                     l+=1
#                     while l<r and nums[l]==nums[l-1]:
#                         l+=1
#                 elif tsum>target:
#                     r-=1
#                     while l<r and nums[r]==nums[r+1]:
#                         r-=1
                
#         return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        current = sum(nums[:k])
        if current >= target:
            return current

        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest