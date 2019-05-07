class Spiral:
    def spiralOrder(self, matrix):
        # 定义四个方向，判定转向
        # 已经选择过的改为“#”
        if not matrix: return []
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        index = 0
        ans = []
        x,y = 0, 0
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m*n):
            ans.append(matrix[x][y])
            matrix[x][y] = '#'
            dx, dy = directions[index][0],directions[index][1]
            if 0 <= x+dx < m and 0<= y+dy < n and matrix[x+dx][y+dy] != "#":
                x = x+dx
                y = y+dy
            else:
                index = (index+1)%4
                dx, dy = directions[index][0],directions[index][1]
                x = x+dx
                y = y+dy               
        return ans