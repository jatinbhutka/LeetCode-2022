# Quick Union - FindUnion (Disjoint Set):

![image](https://user-images.githubusercontent.com/35987583/178134495-5780e4fe-58a8-4f4b-90f6-2e2f1b6a32df.png)


## Why is Quick Union More Efficient than Quick Find?

![image](https://user-images.githubusercontent.com/35987583/178134600-a9fd661a-0463-4047-859f-f45902946cbb.png)


```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
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
![image](https://user-images.githubusercontent.com/35987583/178134614-7795d75d-dc10-4a6f-8173-2904a070e44b.png)

