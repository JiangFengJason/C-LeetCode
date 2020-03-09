class CoinC():
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        init_dp=amount//coins[0]+1
        dp=[init_dp for i in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i]=min(dp[i],1+dp[i-coin])
        if dp[amount]==init_dp:
            return -1
        else:
            return dp[amount]