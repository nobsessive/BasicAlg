class Solution:
    def minDistance_test(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        # bfs approach
        # S is the set of all searched word
        # qu is the queue storing upcoming words
        # num of ops to convert word1 to word2 is equal to the reverse operation, this
        # implementation regard it as convert word2 to word1
        S = {word1}
        l2 = len(word2)
        qu = [[word1, 0]]
        lcl = [ chr(i) for i in range(97, 97+26)] 
        
        def _dist(w1, d, S=S, qu=qu):
            if w1 == word2:
                return d
            l1 = len(w1)
            if l1 < l2:
                # insert
                for i in range(l1+1):
                    for c in lcl:
                        tmp = w1[:i]+c+w1[i:]
                        if tmp not in S:
                            S.add(tmp)
                            qu.append([tmp,d+1])
            elif l1 == l2:
                # replace
                for i in range(l1):
                    if w1[i] != word2[i]:
                        tmp = w1[:i]+word2[i]+w1[i+1:]
                        if tmp not in S:
                            S.add(tmp)
                            qu.append([tmp,d+1])
            else:
                # delete
                for i in range(l1):
                    tmp = w1[:i]+w1[i+1:]
                    if tmp not in S:
                        S.add(tmp)
                        qu.append([tmp,d+1])
            
            return -1
        
        while True:
            ret = _dist(*qu.pop(0))
            if ret != -1:
                return ret
            
testcase = [
    # ["horse", "ros"],
    # ["sea", "eat"],
    ['acbef', 'abdef']
]

ans = [
    # 3,
    # 2,
    2
]

solver = Solution()    
for i in range(len(testcase)):
    res=solver.minDistance_test(*testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")