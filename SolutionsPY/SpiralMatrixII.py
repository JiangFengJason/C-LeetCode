class Sprial:
    def generateMatrix(self, n):
        num=n*n
        l,r,t,b=0,n-1,0,n-1
        matrix=[[0 for i in range(n)] for i in range(n)]
        point=1
        while point <=num:
            for i in range(l,r+1):
                matrix[t][i]=point
                point+=1
            t+=1
            for i in range(t,b+1):
                matrix[i][r]=point
                point+=1
            r-=1
            for i in range(r,l-1,-1):
                matrix[b][i]=point
                point+=1
            b-=1
            for i in range(b,t-1,-1):
                matrix[i][l]=point
                point+=1
            l+=1
        return matrix
