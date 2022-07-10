### Overview of Union-Find (Disjoint Set):

![image](https://user-images.githubusercontent.com/35987583/178125885-0fee9d57-8eaa-47b8-b068-5644e8673d9b.png)
![image](https://user-images.githubusercontent.com/35987583/178126047-ee5328ed-f538-4154-a51f-5604a00b31b5.png)


### Summary of video content:
1. How to implement a “disjoint set”.
2. The find function of a disjoint set.
3. The union function of a disjoint set.

<img width="860" alt="image" src="https://user-images.githubusercontent.com/35987583/178126312-44bf89aa-9b5a-4459-9070-cbb1626c3804.png">


```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

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


<img width="885" alt="image" src="https://user-images.githubusercontent.com/35987583/178126479-b5acd9d7-ff66-45c2-a170-b1ff81e13650.png">
