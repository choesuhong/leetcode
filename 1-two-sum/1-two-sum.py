class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer_dictionary = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in buffer_dictionary:
                return [buffer_dictionary[x], i]
            else:
                buffer_dictionary[nums[i]] = i