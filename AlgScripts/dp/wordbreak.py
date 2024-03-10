# class Solution:
#     def wordBreak_false(self, s: str, wordDict: list[str]) -> bool: 
#           # false: [["catsandog"], ["cats","dog","sand","and","cat", "catsando", "g"] ]
#         # dp method
#         ls, ld = len(s), len(wordDict)
#         dp = [False for _ in range(ls)]
#         for i in range(ls):
#             if dp[i]:
#                 continue
#             if i > 0 and dp[i-1] == False:
#                 break
#             for w in wordDict:
#                 if w == s[i:i+len(w)]:
#                     dp = dp[:i] + [True] * len(w) + dp[i+len(w):]
#                     break
            
#         return dp[ls-1]

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp method
        ls = len(s)
        dp = [False for _ in range(ls+1)]
        dp[0] = True
        for i in range(ls+1):
            dead = 1
            for j in range(i,ls+1):
                if dp[j]==True:
                    for w in wordDict:
                        if w == s[j:j+len(w)]:
                            dp[j+len(w)] = True
                            dead = 0
                    if dp[ls]:
                        return True
                    dp[j] = False
            if dead:
                return False          

        return False

    
testcase = [
    ["leetcode", ["leet","code"]],
    ["applepenapple", ["apple","pen"]],
    ["catsandog", ["cats","dog","sand","and","cat"]],
    ["catsandog", ["cats","dog","sand","and","cat", "catsando", "g"] ]
]

ans = [
    True,
    True,
    False,
    True
]

solver = Solution()
for i in range(len(testcase)):
    res=solver.wordBreak(*testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")
