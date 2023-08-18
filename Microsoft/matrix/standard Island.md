```python
import collections

class Island:
    def __init__(self, grid):
        self.grid = grid
        #self.visited = set()
        
    def isValid(self, x, y):
        return (x in range(len(self.grid)) and y in range(len(self.grid[0]))
                and (x,y) not in self.visited
                and self.grid[x][y] == '1')
        

    def helper_bfs(self, r,c):
        queue = collections.deque()
        queue.append((r,c))
        
        self.visited.add((r,c))
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0, -1]]

        while queue:
            r, c = queue.popleft()
            for dx, dy in DIRECTIONS:
                x, y = r+dx, c+dy
                if self.isValid(x,y):
                    queue.append((x,y))
                    self.visited.add((x,y))
        return


    def noOfIsland(self):
        ROWS = len(self.grid)
        COLS = len(self.grid[0])
        self.visited = set() # to avoid multiple visited at given cell
        no_of_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] == '1' and (r,c) not in self.visited:
                    self.helper_bfs(r,c)
                    no_of_islands += 1
        return no_of_islands
        
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
isLand = Island(grid)
print(isLand.noOfIsland())
```
