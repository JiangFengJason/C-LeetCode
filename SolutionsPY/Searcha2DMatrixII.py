class Searcha2D:
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        x=0
        y=len(matrix[0])-1
        while 0<=x<m and 0<=y<n:
            if matrix[x][y]<target:
                x+=1
            elif matrix[x][y]>target:
                y-=1
            else:
                return True
        return False