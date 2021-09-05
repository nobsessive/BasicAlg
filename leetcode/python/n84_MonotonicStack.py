# find two values for each element, namely left and right
# left is the index of the first smaller height than heights[i] on the left, right is similar
# in this way, ans=max(ans, (right-left-1)*heights[i])
# in addition, we can use monotonic stack to find left and right
class Solution:
    def largestRectangleArea(self, heights) -> int:
        n=len(heights)
        heights.append(-1) # dummy
        left=[-1]*n
        right=[-1]*n
        s=[]
        for i in range(n+1):
            if i==n:
                while s:
                    right[s.pop()]=i #  operation on elements in stack and assure right[n-1]=n # dummy right
            elif s==[] or heights[i]>=heights[s[-1]]:
                s.append(i)
            else: #update max value
                while s and heights[i]<heights[s[-1]]:
                    right[s.pop()]=i
                s.append(i)

        s=[]
        for i in range(n-1,-2,-1):
            if i==-1:
                while s:
                    left[s.pop()]=-1 #  operation on elements in stack and assure right[n-1]=n # dummy left
            elif s==[] or heights[i]>=heights[s[-1]]:
                s.append(i)
            else: #update max value
                while s and heights[i]<heights[s[-1]]:
                    left[s.pop()]=i
                s.append(i)
        left[0]=-1 # dummy left
        maxv=0
        for i in range(n):
            maxv=max(maxv,(right[i]-left[i]-1)*heights[i])
        return maxv
if __name__=="__main__":
    s=Solution() 
    sample=[
        [2,1,2],
        [2,1,5,6,2,3],
        [2,4]
        ]
    '''
    expected=[
        3,
        10,
        4
    ]
    '''
    for i in sample:
        print(s.largestRectangleArea(i))