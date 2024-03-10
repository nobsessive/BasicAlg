class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        p = prices
        l = len(prices)
        inf = 10000+5
        # dp1[j] is the max earning for one trade ending before day j-1
        # dp1[j] = max(dp[j-1], prices[j] - p[i] + dp0[i-1]) =
        # max(.., p[j] - p[i] ) = max(.., p[j] - min(p[i] up to j-1)) =
        # va1 = value(argmin_p[i](min(p[i] up to j-1)))=value(argmin_p[i](f(j)))
        # va1[j] is the j-th value of va1
        # va1[j] = min(va1[j-1], p[j])
        # dp1[j] = max(dp1[j-1], p[j]-va1[j])
        # dp2[j] is the max earning for trade two times before day j-1
        # * let's assume dp2[j] derived from following the same pattern to derive dp1[j]
        #   will also be the best earning for doing at most two trades, i.e., our "best bet". *
        # Then, we have dp2[j] = max(dp2[j-1], p[j]-va2[j]) =?1 max(.., p[j]-min(va2[j-1], p[j])) /* No, it goes back to square 1. This is where we should analyse va2[j] with our tricks. */
        # * It seems va2[j-1] must be updated so that va2[j-1] is indeed 
        # value(argmin_p[i](-dp1[i]+p[i] up to j-2)). We use the trick g(j)=min(g(j-1), job(j)) to do
        # the job. So va2[j]=min(va2[j-1], -dp1[j-1]+p[j]).*
        # The correct answer is the latter. We also see how max earning for one trade pass on to
        # maximum earning for two trades. This has also proved our previous assumption.
        va_j = [ None for _ in range(k)] # anything
        va_jm1 = [p[0] for _ in range(k)] # derived using concrete sample
        dp_j = [0 for _ in range(k)] # prevent cases of l=1, otherwise anything :  dp1_j, dp2_j = None, None
        dp_jm1 = [0 for _ in range(k)] # follow intuition and derived using concrete sample

        for j in range(1,l):
            va_j[0] = min(va_jm1[0], p[j-1])
            dp_j[0] = max(dp_jm1[0], p[j] - va_j[0])
            for i in range(1, k):
                # va2_j = min(va2_jm1, p[j] - dp1_jm1)
                # dp2_j = max(dp2_jm1, p[j]- va2_j)
                va_j[i] = min(va_jm1[i], p[j] - dp_jm1[i-1]) # the second term in min() function need to do the job for j-th index only, since the rest has already been taken care of by va2_jm1
                dp_j[i] = max(dp_jm1[i], p[j] - va_j[i])
            # --
            for i in range(k):
                va_jm1[i], dp_jm1[i] = va_j[i], dp_j[i]

        return dp_j[k-1]

    def maxProfit_2trades(self, prices: list[int]) -> int:
        p = prices
        l = len(prices)
        inf = 10000+5
        # dp1[j] is the max earning for one trade ending before day j-1
        # dp1[j] = max(dp[j-1], prices[j] - p[i] + dp0[i-1]) =
        # max(.., p[j] - p[i] ) = max(.., p[j] - min(p[i] up to j-1)) =
        # va1 = value(argmin_p[i](min(p[i] up to j-1)))=value(argmin_p[i](f(j)))
        # va1[j] is the j-th value of va1
        # va1[j] = min(va1[j-1], p[j])
        # dp1[j] = max(dp1[j-1], p[j]-va1[j])
        # dp2[j] is the max earning for trade two times before day j-1
        # * let's assume dp2[j] derived from following the same pattern to derive dp1[j]
        #   will also be the best earning for doing at most two trades, i.e., our "best bet". *
        # Then, we have dp2[j] = max(dp2[j-1], p[j]-va2[j]) =?1 max(.., p[j]-min(va2[j-1], p[j])) /* No, it goes back to square 1. This is where we should analyse va2[j] with our tricks. */
        # * It seems va2[j-1] must be updated so that va2[j-1] is indeed 
        # value(argmin_p[i](-dp1[i]+p[i] up to j-2)). We use the trick g(j)=min(g(j-1), job(j)) to do
        # the job. So va2[j]=min(va2[j-1], -dp1[j-1]+p[j]).*
        # The correct answer is the latter. We also see how max earning for one trade pass on to
        # maximum earning for two trades. This has also proved our previous assumption.
        va1_j, va2_j = None, None   # anything
        va1_jm1, va2_jm1= p[0], p[0] # derived using concrete sample
        dp1_j, dp2_j = 0, 0 # prevent cases of l=1, otherwise anything :  dp1_j, dp2_j = None, None
        dp1_jm1, dp2_jm1 = 0, 0  # derived using concrete sample
        for j in range(1,l):
            va1_j = min(va1_jm1, p[j-1])
            dp1_j = max(dp1_jm1, p[j] - va1_j)
            va2_j = min(va2_jm1, p[j] - dp1_jm1) # the second term in min() function need to do the job..
            # ..for j-th index only, since the rest has already been taken care of by va2_jm1
            dp2_j = max(dp2_jm1, p[j]- va2_j)
            # --
            va1_jm1, va2_jm1 = va1_j, va2_j
            dp1_jm1, dp2_jm1 = dp1_j, dp2_j
# testcase = [
#     [[1]],
#     [[1,2,3,4,5]],
#     [[7,6,4,3,1]],
#     [[3,3,5,0,0,3,1,4]],
#     [[2,1,2,0,1]],
#     [[1,4,2,7]],
#     [[1,4,2,7,11]]
# ]

# ans = [
#     0,
#     4,
#     0,
#     6,
#     2,
#     8,
#     12
# ]
        return dp2_j
    
testcase = [
    [2, [2,1,4,5,2,9,7]],
    [3, [5, 1, 5, 3, 8, 2, 6]],
    [3, [7, 6, 5, 4, 3, 2, 1]],
    [3, [1,2,3,4,5]],
    [3, [1]],
    [2, [1]],
    [2, [1,2,3,4,5]],
    [2, [7,6,4,3,1]],
    [2, [3,3,5,0,0,3,1,4]],
    [2, [2,1,2,0,1]],
    [2, [1,4,2,7]],
    [2, [1,4,2,7,11]]
]

ans = [
    11,
    13,
    0,
    4,
    0,
    0,
    4,
    0,
    6,
    2,
    8,
    12
]

solver = Solution()    
for i in range(len(testcase)):
    res=solver.maxProfit(*testcase[i])
    if res != ans[i]:
        print(f"wrong@{i}: res = {res}, exp ={ans[i]}")
        continue
    print(f"right: {res}")