# 237. Delete Node in a Linked List

"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
"""

# Solution1: Delete Given Node, by modifiying given node value. Copy next node value to current node
# If you never saw this problem it can seems quite difficult, how you can delete node, if you are given only access to that node? You need to find previous node first? No, the trick is a modification of values in our list! If you have this type of quesitions on real interview, it is the first question you must ask your interviewer. If we can modify data, solution becomes very easy, only two lines: change value of node with value of next node and then change next element for next of next element.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# Time: O(1)
# Space: O(1)
