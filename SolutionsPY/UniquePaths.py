class Unique:
    def uniquePaths(self, m, n):
        meth=[1]*n
        m-=1
        while m:
            for i in range(len(meth)-1):
                meth[i+1]+=meth[i]
            m-=1
        return meth[n-1]