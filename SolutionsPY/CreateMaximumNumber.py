class CreateMaximum:
    def maxNumber(self, nums1, nums2, k):
        def getMax(num,t):
            ans=[]
            size=len(num)
            for x in range(size):
                while ans and size+len(ans)-x>t and ans[-1]<num[x]:
                    ans.pop()
                if len(ans)<t:
                    ans.append(num[x])
            return ans
        
        def Merge(nums1,nums2):
            size1,size2=len(nums1),len(nums2)
            ans=[]
            for x in range(size1+size2):
                if nums1>nums2:
                    ans.append(nums1[0])
                    nums1=nums1[1:]
                else :
                    ans.append(nums2[0])
                    nums2=nums2[1:]
            return ans

        len1,len2=len(nums1),len(nums2)
        res=[]
        for x in range(max(0,k-len2),min(k,len1)+1):
            temp=Merge(getMax(nums1,x),getMax(nums2,k-x))
            res=max(temp,res)
        return res