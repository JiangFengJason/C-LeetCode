class MajorityEl:
    def majorityElement(self, nums):
        count =0
        ready=0

        for num in nums:
            if count==0:
                ready=num
            count+=(1 if ready==num else -1)

        return ready

        # 投机取巧的方法
        # nums=sorted(nums)
        # return nums[len(nums)//2]