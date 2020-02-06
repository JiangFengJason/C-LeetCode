class CombinationS:
    def combinationSum(self, candidates, target):
        path =[]
        res =[]
        candidates.sort()
        self.reCombination(res,0,target,candidates,path)
        return res
        
    
    def reCombination(self, res, begin, target,candidates,path):
        if target==0:
            res.append(path[:])
        
        for index in range(begin,len(candidates)):
            rest=target-candidates[index]
            if rest<0:
                break
            path.append(candidates[index])
            self.reCombination(res,index,rest,candidates,path)
            path.pop()