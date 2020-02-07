import collections
class GroupAnag:
    def groupAnagrams(self, strs):
        ans=collections.defaultdict(list)
        # 按照顺序进行字典key的确定
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)

        # 按照大小激行确定
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            ans[tuple(count)].append(s)
        return ans.values()