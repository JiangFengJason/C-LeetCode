class SumClosest:
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        triple=nums[0]+nums[1]+nums[-1]
        diff=abs(triple-target)
        for i in range(0,len(nums)-2):
            if i==0 or nums[i-1]!=nums[i]:
                l=i+1
                r=len(nums)-1
                while l<r:
                    s=nums[l]+nums[r]+nums[i]
                    d=abs(s-target)
                    if d<diff:
                        diff=d
                        triple=s
                    if s==target:
                        return target
                    elif s<target:
                        l+=1
                    else :
                        r-=1
        return triple                    