# two pointers iterate through an 1-D array
# while(left < right)
#   if(move conition left)
#       set cursor
#       move left pointer
#       f(cursor)
#   elif(move condition right)
#       same as above
class Solution:
    def trap(self, height) -> int:
        n=len(height)
        if n<3:
            return 0
        ans=0
        max_left,max_right=height[0],height[-1]
        left,right=0,n-1
        while(left<right):#
            if height[left]<height[right]:
                cur=left+1
                left+=1
                if height[cur]<max_left:
                    ans+=max_left-height[cur]
                else:
                    max_left=height[cur]
            else:
                cur=right-1
                right-=1
                if height[cur]<max_right:
                    ans+=max_right-height[cur]
                else:
                    max_right=height[cur]
        return ans
if __name__=="__main__":
    s=Solution()
    sample=[
        [4,2,0,3,2,5],
        [0,1,0,2,1,0,1,3,2,1,2,1]
        ]
    for i in sample:
        print(s.trap(i))