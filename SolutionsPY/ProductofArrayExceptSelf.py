class ProductofArray:
    def productExceptSelf(self, nums):
        res,p,q=[1],1,1
        for i in range(len(nums)-1):
            p*=nums[i]
            res.append(p)
        for i in range(len(nums)-1,0,-1):
            q*=nums[i]
            res[i-1]*=q
        return res