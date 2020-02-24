class LongestIncreasingSub:
    def lengthOfLIS(self, nums):
        if len(nums)==0:
            return 0
        dp=[1]*len(nums)
        for i in range(len(dp)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)