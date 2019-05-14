class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class MergeInter:
    def merge(self, intervals):
        intervals = sorted(intervals,key = lambda k:k.start)
        res = []
        for i in intervals:
            if res and res[-1].end >= i.start:
                res[-1].end = max(res[-1].end,i.end)
            else:
                res.append(i)
        return res
                
