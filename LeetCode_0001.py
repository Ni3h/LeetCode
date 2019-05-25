"""
Solution to LeetCode_0001 - Two Sum
Brute force method!
@author - Ni3h
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Loop through the list
        for i in nums:
            goal = target - i
            #Loop through the remaining numbers, have to use .index because
            # initial loop is for x in y.
            for j in range(nums.index(i)+1, len(nums)):
                if goal == nums[j]:
                    return [nums.index(i), j]


#test Testadasda