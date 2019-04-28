# 在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
# 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）逆序排列。
# 比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
# 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。

class NextPer:
    def nextPermutation(self, nums) -> None:
        if len(nums) <= 1: return nums
        partition = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                partition = i
                break
        if partition == -1: 
            nums.reverse()
            return nums
        else:
            for i in range(len(nums)-1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i],nums[partition] = nums[partition],nums[i]
                    break
        left = partition+1; right = len(nums)-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1; right-=1
        return nums