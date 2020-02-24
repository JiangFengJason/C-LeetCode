import sys
class BestTimetoButandSellStock:
    def maxProfit(self, prices):
        n=len(prices)
        dp_i_0=0
        dp_i_1=-sys.maxsize
        dp_pre=0
        for i in range(n):
            temp=dp_i_0
            dp_i_0=max(dp_i_0,dp_i_1+prices[i])
            dp_i_1=max(dp_i_1,dp_pre-prices[i])
            dp_pre=temp
        return dp_i_0