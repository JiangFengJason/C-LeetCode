class NumberofIs:
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    def numIslands(self, grid):
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        marked=[[False for _ in range(n)]for _ in range(m)]
        count=0
        for i in range(0,m):
            for j in range(0,n):
                if marked[i][j]==False and grid[i][j]=="1":
                    self.isIsland(m,n,marked,grid,i,j)
                    count+=1
        return count

    def isIsland(self,m,n,marked,grid,i,j):
        marked[i][j]=True
        for direction in self.directions:
            new_x=i+direction[0]
            new_y=j+direction[1]
            if 0<=new_x<m and 0<=new_y<n and not marked[new_x][new_y] and grid[new_x][new_y]=="1":
                self.isIsland(m,n,marked,grid,new_x,new_y)