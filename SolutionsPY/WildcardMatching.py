class Wildcard:
    def isMatch(self,s,p):
        n=len(s)
        m=len(p)
        record = [ [False] * (n+1) for i in range(m+1)] 
        record[0][0]=True
        for k in range(1,m+1):
            record[k][0]=record[k-1][0] and p[k-1]=="*"
        for j in range(m):
            for i in range(n):
                if s[i]==p[j] or p[j]=="?":
                    record[j+1][i+1]=record[j][i]
                elif p[j]=="*":
                    record[j + 1][i + 1] = record[j][i + 1] or record[j+1][i]
                else:
                    record[j + 1][i + 1] = 0
        return record[m][n]