class SearchinRotatedSorted:
    def search(self, nums, target):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            if nums[mid]>=nums[start]:
                if target>=nums[start] and target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            
            if nums[mid]<=nums[end]:
                if target<=nums[end] and target>nums[mid]:
                    start=mid+1
                else:
                    end=mid-1
        return -1