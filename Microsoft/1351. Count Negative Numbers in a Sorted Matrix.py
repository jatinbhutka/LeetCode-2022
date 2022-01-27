"""
# 1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid. 

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

Follow up: Could you find an O(n + m) solution?

"""


#Solution 1: Brute Force.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
        return count
      
    
    
# Time: O(N*M)
# Space: O(1)






#Solution 2: optimized Using pattern

"""
This solution uses the fact that the negative regions of the matrix will form a "staircase" shape, e.g.:

++++++
++++--
++++--
+++---
+-----
+-----
What this solution then does is to "trace" the outline of the staircase.
Start from ***bottom-left*** corner of the matrix, count in the negative numbers in each row.

"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid)-1, 0
        count = 0
        
        while row >= 0 and col < len(grid):
            if grid[row][col] < 0:
                count += len(grid[0]) - col
                row -= 1
            else:
                col += 1
        return count

# Time: O(N+M)
# Space: O(1)












#Solution 3: optimized using binary search 
# Since each row is in sorted order, Pass each row for binary search and count the negatives

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary(arr):
            start = 0
            end = len(arr)
            while start < end:
                mid = start + ((end - start))//2
                if arr[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(arr) - start
        
        count = 0
        for i in range(len(grid)):
            count += binary(grid[i])
        return count

# Time: O(N LogM)
# Space: O(1)
