class GasStat:
    def canCompleteCircuit(self, gas, cost):
        total=0
        curr=0
        flag=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            curr+=gas[i]-cost[i]
            if curr<0:
                curr=0
                flag=i+1
        return flag if total>=0 else -1