# Given an array of intergers, the indices of two numbers that add up to a specific target 
# is added. Only one solution exists for each array, and elements are not repeatedly used

class Solution:
    def twoSum(nums, target: int):
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if target == nums[i]+nums[j]:
                    return [i, j]
        return None
    
    print(twoSum([1,2,4], 5))