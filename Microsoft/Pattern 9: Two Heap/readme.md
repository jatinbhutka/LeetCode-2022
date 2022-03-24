# Introduction:

In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an efficient approach to solve such problems.

As the name suggests, this pattern uses two Heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element.

```python
from heapq import *


# Push to heap:
heappush(self.minHeap, num)

# Pop min element of heap
heappop(self.minHeap)
```


<img width="612" alt="image" src="https://user-images.githubusercontent.com/35987583/159852766-77674f1f-0139-4c6c-b6ca-121ebdd80fc5.png">
