class FindFirstandLastPosition:
    def searchend(self,nums,target,left):
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if nums[mid]>target or (left and nums[mid]==target):
                high=mid
            else:
                low=mid+1
        return low

    def searchRange(self, nums, target):
        left=self.searchend(nums,target,True)
        if left==len(nums) or nums[left]!=target:
            return [-1,-1]
        return [left,self.searchend(nums,target,False)-1]