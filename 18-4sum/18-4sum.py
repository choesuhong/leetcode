class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l = j+1
                r = len(nums)-1
                while l<r:
                    while l<r and nums[i]+nums[j]+nums[l]+nums[r]<target:
                        l+=1
                    while l<r and nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                    if l<r and nums[i]+nums[j]+nums[l]+nums[r]==target:
                        if not [nums[i],nums[j],nums[l],nums[r]] in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                
        return res