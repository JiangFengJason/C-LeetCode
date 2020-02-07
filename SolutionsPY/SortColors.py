class SortColor:
    def sortColors(self, nums):
        index=0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]==0:
                nums[index],nums[l]=nums[l],nums[index]
                index+=1
                l+=1
            elif nums[l]==2:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return nums