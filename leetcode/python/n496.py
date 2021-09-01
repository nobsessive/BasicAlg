# monotonic stack
# iterate through nums[i]
#   while s and s[-1] <nums[cur]:
#       add influence of cur to s
#   update s, cur
class Solution:
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        s=[] # stack
        cur=0
        while cur<n:
            while s and nums[s[-1]]<nums[cur]:
                ans[s.pop()]=nums[cur]
            s.append(cur)
            cur+=1
        cur=0
        while cur<n:
            while s and nums[s[-1]]<nums[cur]:
                u=s.pop()
                if ans[u]==-1:
                    ans[u]=nums[cur]
            s.append(cur)
            cur+=1
        return ans
    # approximate solution
    def nextGreaterElements_non_circularly(self, nums):
        n=len(nums)
        ans=[-1]*n
        s=[] # stack
        cur=0
        while cur<n:
            while s and nums[s[-1]]<nums[cur]:
                ans[s.pop()]=nums[cur]
            s.append(cur)
            cur+=1
        return ans
if __name__=="__main__":
    s=Solution()
    sample=[
        [1,2,1],
         [1,2,3,4,3]
        ]
    for i in sample:
        print(s.nextGreaterElements(i))