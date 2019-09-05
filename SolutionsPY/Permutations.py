class Permu:
    def permute(self, nums):
        n=len(nums)
        output=[]

        def exchange(first=0):
            if first==n:
                output.append(nums[:])
            for i in range(first,n):
                nums[i],nums[first]=nums[first],nums[i]
                exchange(first+1)
                nums[i],nums[first]=nums[first],nums[i]
        
        exchange()
        return output