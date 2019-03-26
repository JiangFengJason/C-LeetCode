class climb:
    def climbStairs(self, n: int) -> int:
        count=[0]*(n+1)
        count[0]=1
        count[1]=1
        i=2
        while i<=n:
            count[i]=count[i-1]+count[i-2]
            i+=1
        return count[-1]