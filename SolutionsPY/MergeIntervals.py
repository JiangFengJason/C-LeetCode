class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class MergeInter:
    def merge(self, intervals):
        intervals = sorted(intervals,key = lambda k:k[0])
        res = []
        for i in intervals:
            if res and res[-1][-1] >= i[0]:
                res[-1][-1] = max(res[-1][-1],i[-1])
            else:
                res.append(i)
        return res
                
