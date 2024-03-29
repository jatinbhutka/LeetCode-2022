"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# Solution 1:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            max_sum = max(temp_sum, max_sum)
        return max_sum
# Time: O(N)
# Space: O(1)



# Counter Question: Maximum Subarray with maximum Sum:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        maxSum = nums[0]
        
        start = end = 0
        
        for i in range(1,len(nums)):
            
            if currSum + nums[i] < nums[i]:
                big = i
            currSum = max(currSum + nums[i], nums[i])
            
            if maxSum < currSum:
                start = big
                end = i
            maxSum = max(currSum, maxSum)
        return nums[start:end+1]



# Solution 1: optimized Bruter Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
# Time: O(N^2)
# Space: O(1)
