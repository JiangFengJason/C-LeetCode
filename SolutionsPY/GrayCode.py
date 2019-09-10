class Gray:
    def grayCode(self, n):
        if n==0:
            return [0]
        res=[]
        def search(num,x):
            if len(num)==n:
                res.append(int(num,2))
            elif x==0:
                search(num+'0',0)
                search(num+'1',1)
            else:
                search(num+'1',0)
                search(num+'0',1)
        search('',0)
        return res