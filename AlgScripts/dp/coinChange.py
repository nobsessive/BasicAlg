class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        inf = 10005 # 10^4+5 greater than amount
        dp = [inf for _ in range(amount+1)]
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        def _coinChange(coins=coins, amount=amount, dp=dp):
            print(f"amount {amount}, dp {dp}")
            if dp[amount] < inf :   # -1 or visited
                return dp[amount]
            mins = inf 
            for c in coins:
                if c<=amount:
                    rec_ret = _coinChange(coins, amount-c, dp)
                    if rec_ret!= -1 and rec_ret + 1 < mins:
                        mins = rec_ret+1
            dp[amount] = -1 if mins == inf else mins
            return dp[amount]

        return _coinChange(coins, amount, dp)

testcase = [
    # [[1, 2, 5], 11],
    # [[2], 3],
    # [[1,2,5], 100], 
    [[2,5,10,1], 27]   
]

ans = [
    # 3,
    # -1,
    # 20,
    4
]

solver = Solution()    
for i in range(len(testcase)):
    res=solver.coinChange(*testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")