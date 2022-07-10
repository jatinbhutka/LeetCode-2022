# Path Compression Optimization - Union Find(Disjoint Sets):

<img width="828" alt="image" src="https://user-images.githubusercontent.com/35987583/178137269-139e1020-e624-4ff1-99ac-9d03f7aeeb7b.png">

<img width="828" alt="image" src="https://user-images.githubusercontent.com/35987583/178137308-327f3c87-ccb2-4b1d-be64-e7a716fe730b.png">


<img width="810" alt="image" src="https://user-images.githubusercontent.com/35987583/178137362-a4872de4-c57a-4a22-a8d6-57dcd61ede55.png">



```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
```



<img width="852" alt="image" src="https://user-images.githubusercontent.com/35987583/178137372-16df8bbc-9603-451c-93f9-0d79cce2218c.png">

        return self.root[x]
