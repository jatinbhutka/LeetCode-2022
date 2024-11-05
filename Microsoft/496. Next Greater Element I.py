# 496. Next Greater Element I:


```py
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {num : i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        
        for ind, num in enumerate(nums2):
            while stack and num > stack[-1]:
                prevNo = stack.pop()
                if prevNo in hashMap:
                    result[hashMap[prevNo]] = num
            stack.append(num)
        return result
```

"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""


"""
Steps:

- We traverse nums2 and start storing elements on the top of stack.
- If current number is greater than the top of the stack, then we found a pair. Keep popping from stack till the top of stack is smaller than current number.
- After matching pairs are found, push current number on top of stack.
- Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't found for them. Hence we'll put -1 for the remaining elements in stack.
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        stack = []
        mapper = {}
        stack.append(nums2[0])
        
        for i in range(1,len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                mapper[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
                
        if len(stack) > 0:
            for ele in stack:
                mapper[ele] = -1

        for ele in nums1:
            res.append(mapper[ele])
    
        return res


# Complexity Analysis:

# Let n and m represent the length of the nums2 and nums1 array respectively.

# Time complexity: O(n). 
# The entire nums2 array (of size n) is scanned only once. Each of the stack's n elements are pushed and popped exactly once. The nums1 array is also scanned only once. All together this requires O(n + n + m)O(n+n+m) time. Since nums1 must be a subset of nums2, we know m must be less than or equal to n. Therefore, the time complexity can be simplified to O(n).

# Space complexity: O(n) 
# Map will store n key-value pairs while stack will contain at most n elements at any given time.
