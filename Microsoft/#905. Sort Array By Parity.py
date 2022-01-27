"""
#905. Sort Array By Parity


Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""

# Solution 1: Using Two Pointer

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        odd = len(nums)-1
        while even < odd:
            if nums[even]%2==0:
                even += 1
            else:
                nums[even], nums[odd] = nums[odd],nums[even]
                odd -= 1
        return nums
      
# Time: O(N)
# Space: O(1)
