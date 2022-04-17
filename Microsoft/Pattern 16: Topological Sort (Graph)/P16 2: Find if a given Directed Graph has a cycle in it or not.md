# P16 2: Find if a given Directed Graph has a cycle in it or not:

```python
from collections import deque


def detectCycleInDirectedGraph(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # Initialize vertices Count:
  inDegreeCount = {}
  for i in range(vertices):
      inDegreeCount[i] = 0

  # a. Initialize parent to # Child:
  parent_child = {}
  for i in range(vertices):
      parent_child[i] = []
      
  
  # b. Build inDegreeCount, parent_child:
  for edge in edges:
      parent = edge[0]
      child = edge[1]
      parent_child[parent].append(child)
      inDegreeCount[child] += 1
      
  # c. Find all sources i.e., all vertices with 0 in-degrees
  source = deque()
  for key in inDegreeCount:
      if inDegreeCount[key] == 0:
          source.append(key)
          
  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees if a child's in-degree becomes zero, add it to the sources queue
  
  while len(source) > 0:
      vertex = source.popleft()
      sortedOrder.append(vertex)
      
      for child in parent_child[vertex]:
        inDegreeCount[child] -= 1
        if inDegreeCount[child] == 0:
            source.append(child)
            
  if len(sortedOrder) != vertices:
    return True
  return False
            

  

def main():
  print("Topological sort: " +
        str(detectCycleInDirectedGraph(2, [[0,1], [1,0]])))
  print("Topological sort: " +
        str(detectCycleInDirectedGraph(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(detectCycleInDirectedGraph(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()

```

### Time: O(V + N)
### Space: O(V + N)
