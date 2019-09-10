class MergeSortedArra:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1[:]=sorted(nums1)
        #res=sorted(nums1)
        #return res