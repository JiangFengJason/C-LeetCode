import collections
class ContainsDu:
    def containsDuplicate(self, nums):
        counter=collections.Counter(nums)
        key=list(counter)
        for item in key:
            if counter[item] != 1:
                return True
        return False