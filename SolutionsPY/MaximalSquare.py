class Maximal:
    def maximalSquare(self, matrix):
        n=len(matrix)
        if n==0:
            return 0
        m=len(matrix[0])
        maxim=0
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxim=max(maxim,dp[i][j])
        return maxim*maxim