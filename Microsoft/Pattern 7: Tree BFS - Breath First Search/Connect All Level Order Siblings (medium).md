# Connect All Level Order Siblings (medium):

Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.



<img width="995" alt="image" src="https://user-images.githubusercontent.com/35987583/158787703-3265e16a-5d34-45d7-81c6-9f15dd9936e2.png">


```python
from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  # TODO: Write your code here
  if root is None:
    return None
  
  queue = [root]
  next_queue = []
  original_root = root
  prevNode = TreeNode(-1)
  prevNode.next = root

  while len(queue) > 0:
      
      for root in queue:
          
          if prevNode:
              prevNode.next = root
          prevNode = root
          
          if root.left:
              next_queue.append(root.left)
          if root.right:
              next_queue.append(root.right)
      queue = next_queue
      next_queue = []
  return original_root


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()

```


```python
from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  currentNode, previousNode = None, None
  while queue:
    currentNode = queue.popleft()
    if previousNode:
      previousNode.next = currentNode
    previousNode = currentNode

    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()

```

#### Time complexity: O(N)
where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

#### Space complexity: O(N)
The space complexity of the above algorithm will be O(N) which is required for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.
