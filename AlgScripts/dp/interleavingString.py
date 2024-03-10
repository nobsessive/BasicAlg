class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # - special cases
        if s3 == "":
            return True
        ls, l1, l2 = len(s3), len(s1), len(s2)
        if ls != l1 + l2:
            return False
        # begin dp
        s = s3
        # dp[i][j] is 1 if s[i+j .. ls] is an interleaving of s1[i..l1] and s2[j..l2]
        dp=[[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        dp[l1][l2] = 1

        def _func(i, j, dp=dp):
            if dp[i][j] != -1:
                return bool(dp[i][j])
            if i==l1:
                dp[i][j] = s2[j]==s[l1+j] and _func(i, j+1)
            elif j==l2:
                dp[i][j] = s1[i]==s[i+l2] and _func(i+1, j)
            else:
                dp[i][j] = (s[i+j] == s1[i] and _func(i+1, j) ) or \
                    ( s[i+j]==s2[j] and  _func(i, j+1))
            return bool(dp[i][j])

        return _func(0, 0)
    
    # Following code actually tries to solve a harder problem : s3 is an interleaving of substring of s1 and/or substring of s2.
    # Practically, it is a result from neglegation of the fact that ls must be equal to l1 + l2 rather than ls <= l1 + l2 according
    # to problem statement
    def isInterleave_fail_2(self, s1: str, s2: str, s3: str) -> bool:
        # - special cases
        if s3 == "":
            return True
        ls, l1, l2 = len(s3), len(s2), len(s2)
        if ls > l1 + l2:
            return False
        # begin dp
        s = s3
        # dp1[i][j] represents the option to cover s[i] with string ending at s1[j] made available by using s2 up to index dp1[i][j]
        dp1, dp2 = [[-1 for _ in range(l1)] for _ in range(ls)], [[-1 for _ in range(l2)] for _ in range(ls)]
        # max1 is the maximum index that has already been used in dp1[i]
        max1, max2 = [-1 for _ in range(l1)]
        # cover s[i] using string ending at s_t
        def _func(i, t):
            if t==1:
                if i ==0:
                    pass
                else:
                    for j in range(l1-1):
                        if dp1[i-1][j] == 1 and s1[j+1]==s[i]:
                            dp1[i][j+1] = 1
                            return 1
                    p = -1
                    for j in range(l2):
                        if dp2[i-1][j] == 1:
                            pass


    # Following  func is the initial thought of mine which is incorrect
    # In main for loop, at "if dp1[i-1] != 1" block, I was trying to update both
    # dp1[i] and dp2[i]. If both attempts succeded, it will rule out the possibility to use s2[dp2[i]]
    # in the future when s1[dp1[i]] has already done the job.
    def isInterleave_fail(self, s1: str, s2: str, s3: str) -> bool:
        # - special cases
        if s3 == "":
            return True
        ls, l1, l2 = len(s3), len(s2), len(s2)
        if ls > l1 + l2:
            return False
        # begin dp
        s = s3
        # dp1[i] represents the option to cover s3[i] with substr ending at s1[dp1[i]]
        dp1, dp2 = [-1 for _ in range(ls)], [-1 for _ in range(ls)]
        p1, p2 = 0, 0 # pointers indicating s1[p1:] still available
        for i in range(l1):
            if s1[i]==s[0]:
                dp1[0] == i
                p1 = i+1
        for i in range(l2):
            if s2[i]==s[0]:
                dp2[0] == i  
                p2 = i+1
        # main for loop
        for i in range(1,ls):
            if dp1[i-1] == -1 and dp2[i-1] == -1:
                return False
            if dp1[i-1] != -1:
                if j+1 < l1 and s[i]==s1[j+1]:
                    dp1[i]=j+1
                    p1 = j+2
                if dp2[i-1]!=1:
                    for k in range(p2, l2):
                        if s[i]==s2[k]:
                            dp2[i]=k
                            p2 = k+1
                            break
            if dp2[i-1]:
                for j in dp2[i-1]:
                    if j+1 < l2 and s[i]==s2[j+1]:
                        dp2[i].append(j+1)
                        break
                if dp1[i-1]:
                    for k in range(min(dp1[i-1]), l1):
                        if s[i]==s1[k]:
                            dp1[i].append(k)
                            break

        return True if dp1[ls-1] or dp2[ls-1] else False
    
testcase = [
    ['s', '', 's']  
]

ans = [
    True
]

solver = Solution()    
for i in range(len(testcase)):
    res=solver.isInterleave(*testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")