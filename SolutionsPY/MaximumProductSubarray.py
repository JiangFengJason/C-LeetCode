import sys
class MaximumProdect:
    def maxProduct(self, nums):
        imax=1
        imin=1
        Max=-sys.maxsize
        for num in nums:
            if num<0:
                imax,imin=imin,imax
            imax=max(imax*num,num)
            imin=min(imin*num,num)
            Max=max(imax,Max)
        return Max