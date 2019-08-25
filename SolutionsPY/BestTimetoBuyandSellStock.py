class BestTimetoBuy:
    def maxProfit(self, prices):
        betw=0
        temp=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                if i==0:
                    temp=max(prices[i+1:len(prices)])-prices[0]
                elif i==len(prices)-2:
                    temp=prices[-1]-min(prices[0:i+1])
                else:
                    temp=max(prices[i+1:len(prices)])-min(prices[0:i+1])
                if temp>betw:
                    betw=temp
        return betw
        