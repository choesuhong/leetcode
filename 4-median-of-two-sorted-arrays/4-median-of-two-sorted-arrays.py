class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)
        
        if N1 < N2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        lo, hi = 0, 2*N2
        while lo<=hi:
            mid2 = (lo+hi)//2
            mid1 = N1 + N2 - mid2
            
            L1 = nums1[(mid1-1)//2] if mid1 != 0 else float('-inf')
            L2 = nums2[(mid2-1)//2] if mid2 != 0 else float('-inf')
            R1 = nums1[mid1//2] if mid1 != 2*N1 else float('inf')
            R2 = nums2[mid2//2] if mid2 != 2*N2 else float('inf')
            
            if L1>R2:
                lo = mid2 + 1
            elif L2>R1:
                hi = mid2 - 1
            else:
                return (max(L1,L2)+min(R1,R2))/2
                