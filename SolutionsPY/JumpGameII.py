class JumpG:
    def toJump(self,nums):
        lastRc,currentRc,count,Len=0,0,0,len(nums)
        for i in range(Len):
            if lastRc<i:
                lastRc=currentRc
                count+=1
            currentRc=max(currentRc,nums[i]+i)
        return count