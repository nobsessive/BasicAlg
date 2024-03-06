class Solution:
    def longestPalindrome_failed(self, s: str) -> str:
        # dynamic programming approach
        # following previous submit error!
        # in order to avoid the error, we need to store the length of max palindrome ending at index i
        ls = len(s)
        if ls < 2:
            return s
        dp = [0]*ls
        dp[0] = 1
        m, m_idx = 1, 0   # longest palindrome, end index
        for i in range(1, ls-1):
            m_i, start_i = dp[i-1], i-dp[i-1]+1
            if start_i-1 >= 0 and s[i] == s[start_i-1]:  # longest new palindrome
                dp[i] = dp[i-1]+2
                if dp[i] > m:
                    m, m_idx = dp[i], i
            else:
                pass

    def longestPalindrome(self, s: str) -> str:
        ls=len(s)
        dp = [ [0 for _ in range(ls)] for _ in range(ls)]
        m, midx = 0, [-1, -1]
        for i in range(ls):
            for j in range(i+1):
                if s[j]==s[i] and ((j+1 >= i) or (j+1<ls and dp[j+1][i-1])):
                    dp[j][i] = 1
                    if i-j+1 > m:
                        m = i-j+1
                        midx = [j, i]
        return s[midx[0] : midx[1]+1]


    
testcase =[
    'cbbd',
    'babad',
    'csdbbdsd',
    'ac',
    'ccd', 
    'bb',    
    'aaaa',  
    'bananas',
    'dabbcd'
] 

ans = [
    'bb',
    'bab',
    'sdbbds',
    'a',
    'cc',
    'bb',
    'aaaa',
    'anana',
    'bb'
]


# solver = Solution1()
# for i in testcase:
#     print(solver.longestPalindrome(i))

def longestPalindrome(s: str) -> str:
    ls=len(s)
    dp = [ [0 for _ in range(ls)] for _ in range(ls)]
    m, midx = 0, [-1, -1]
    for i in range(ls):
        for j in range(i+1):
            if s[j]==s[i] and ((j+1 >= i) or (j+1<ls and dp[j+1][i-1])):
                dp[j][i] = 1
                if i-j+1 > m:
                    m = i-j+1
                    midx = [j, i]
    return s[midx[0] : midx[1]+1]
    
    

for i in range(len(testcase)):
    res=longestPalindrome(testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")
