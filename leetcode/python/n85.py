# see notes on 09/02/2021 -- pattern of monotonic stack
class Solution:
    # n85 solution
    def maximalRectangle(self, matrix) -> int:
        # special cases
        if not matrix or not matrix[0]:
            return 0
        ans=0
        r,c=len(matrix),len(matrix[0])
        height=[0]*(c+1)
        for i in range(r):
            for j in range(c):
                height[j]=height[j]+1 if matrix[i][j]=='1' else 0
            # find the max rectangle in histogram height
            s=[-1]
            for j in range(c+1):
                while height[s[-1]]>height[j]:
                    h=height[s.pop()]
                    w=j-s[-1]-1
                    ans=max(ans,h*w)
                s.append(j)
        return ans
    # very neat solution to a sub-problem, ref https://leetcode.com/problems/maximal-rectangle/discuss/1434675/Python-based-on-largest-rectangle-in-histogram 
    # element in stack are arranged with rules as coded can achieve following goals:
    # 1. e[i-1] is the first element less than or equal to e[i] (e[i] is top of the stack)
    # -> 1. so j-e[i-1]-1 is the length of the rectangle
    # 2. dummy element -1 is pushed into the stack while height[-1] is defined as the smallest value
    # -> 1. stack is never empty, at least -1 is always in the stack
    # -> 2. rule 1->1 is guranteed when there is only -1 in the stack, j-e[i-1]-1 = j-(-1)-1 = j
    def maximalRectangle_ref(self, heights) -> int:
        m=len(heights)
        heights.append(0)
        stack=[-1]
        res=0
        for j in range(m+1):
            while heights[stack[-1]] > heights[j]:
                prev_height = heights[stack.pop()]
                width = j - stack[-1] - 1
                res = max(res, width * prev_height)
            stack.append(j)
        return res

if __name__=="__main__":
    s=Solution() 
    #print(s.maximalRectangle_ref([3,2,1,0,5,4,3,1]))
    
    sample=[
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        ]
    expected=[
        6
    ]
    for i in sample:
        print(s.maximalRectangle(i))
    