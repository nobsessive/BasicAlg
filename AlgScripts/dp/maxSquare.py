class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # let dp[i-1][j], dp[i][j-1] == p, q and p>=q
        # dp[i][j] = q+1 when p>q else q + int(matrix[i-q][j-q])
        maxr = int(matrix[0][0])
        m, n = len(matrix), len(matrix[0])
        for i in range(1,m):
            if matrix[i][0] == '1':
                maxr = 1
                break
        if maxr != 1:
            for j in range(1,n):
                if matrix[0][j] == '1':
                    maxr = 1
                    break
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    #print(f"{i}, {j}, {matrix}")
                    c = min(int(matrix[i-1][j]), int(matrix[i][j-1]))
                    matrix[i][j] = 1 if c==0 else c+int(bool(int(matrix[i-c][j-c])))
                    maxr = max(matrix[i][j], maxr)
        
        return maxr**2
    

testcase = [
    # [[["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]],
    # [[["1","0","1","0","0","1","1","1","0"],
    #   ["1","1","1","0","0","0","0","0","1"],
    #   ["0","0","1","1","0","0","0","1","1"],
    #   ["0","1","1","0","0","1","0","0","1"],
    #   ["1","1","0","1","1","0","0","1","0"],
    #   ["0","1","1","1","1","1","1","0","1"],
    #   ["1","0","1","1","1","0","0","1","0"],
    #   ["1","1","1","0","1","0","0","0","1"],
    #   ["0","1","1","1","1","0","0","1","0"],
    #   ["1","0","0","1","1","1","0","0","0"]]],
    [[["1","1","1","1","0"],
      ["1","1","1","1","0"],
      ["1","1","1","1","1"],
      ["1","1","1","1","1"],
      ["0","0","1","1","1"]]]
]

ans = [
    # 4,
    # 4,
    16
]

solver = Solution()    
for i in range(len(testcase)):
    res=solver.maximalSquare(*testcase[i])
    if res != ans[i]:
        print(f"wrong: {i}, res = {res}")
        continue
    print(f"right: {res}")