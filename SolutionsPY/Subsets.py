class SubSet:
    def subsets(self, nums):
        res=[]
        n=len(nums)

        def helper(i,temp):
            res.append(temp)
            for j in range(i,n):
                helper(j+1,temp+[nums[j]])
        helper(0,[])
        return res