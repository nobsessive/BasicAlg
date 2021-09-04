'''
In select() function:
    while ... and cnt+n-i>k and ...:
        - n=5, i=4, 4+5-4==5, can't pop. So equation must use >.
In merge() function:
    - compare two lists rather than first two elements
    - ans.append(l.pop(0)) must be used since l should also be changed
'''
class Solution:
    def maxNumber(self, nums1 , nums2, k: int):
        def select(l,k):
            if k<1:
                return []
            cnt=0 # numbers in stack
            s=[] # stack
            n=len(l)
            for i in range(n):
                while s and cnt+n-i>k and s[-1]<l[i]:
                    s.pop()
                    cnt-=1
                if cnt<k:
                    s.append(l[i])
                    cnt+=1
            return s
        def merge(l,k,r):
            ans=[]
            p,q=0,0
            m,n=len(l),len(k)
            while p!=m and q!=n:
                if l>k:
                    ans.append(l.pop(0))
                    p+=1
                else:
                    ans.append(k.pop(0))
                    q+=1
            if p==m:
                ans=ans+k
            else:
                ans=ans+l
            if ans>r:
                return ans
            else:
                return r
        m,n=len(nums1),len(nums2)
        if k>m+n:
            return []
        ans1,ans2,ans=[],[],[]
        for i in range(min(k,n)+1):
            if k-i>m:
                continue
            ans1=select(nums1,k-i)
            ans2=select(nums2,i)
            ans=merge(ans1,ans2,ans)
        return ans
    def maxNumber_fail1(self, nums1 , nums2, k: int):
        ans=[]
        m,n=len(nums1),len(nums2)
        p,q=0,0
        while p!=m or q!=n:
            r=m-p+n-q # numbers left to proceed
            if len(ans)+r==k:
                break
            if p!=m and (q==n or nums1[p]>nums2[q]):
                while ans and ans[-1][1]<nums1[p]:
                    t=ans.pop()
                    if t[0]==1 and t[1]==q-1: # move q backward
                        q-=1
                    k+=1
                ans.append((0,p))
                p+=1
            else:
                while ans and ans[-1][1]<nums2[q]:
                    t=ans.pop()
                    if t[0]==0 and t[1]==p-1: # move p backward
                        p-=1
                    k+=1
                ans.append((1,nums2[q]))
                q+=1
        while 1:
            if p==m and q==n:
                break
            if  p==m:
                ans.append((1,nums2[q]))
                q+=1
                continue
            elif q==n:
                ans.append((0,nums1[p]))
                p+=1
                continue
            
            if nums1[p]>nums2[q]:
                ans.append((0,nums1[p]))
                p+=1
                continue
            elif nums1[p]<nums2[q]:
                ans.append((1,nums2[q]))
                q+=1
                continue
            r,s=p,q
            while  r!=m and s!=n and nums1[r]==nums2[s]:
                r+=1
                s+=1
            if r==m and s==n: # add everything to ans
                while p!=m:
                    ans.append((0,nums1[p]))
                    p+=1
                while q!=n:
                    ans.append((1,nums2[q]))
                    q+=1
                break
            elif (r==m and nums2[s]>nums1[p]):
                while q<=s:
                    ans.append((1,nums2[q]))
                    q+=1
            elif (s==n and nums1[r]>nums2[q]):
                while p<=r:
                    ans.append((0,nums1[p]))
                    p+=1
            elif nums1[r]>nums2[s]:
                while p<=r:
                    ans.append((0,nums1[p]))
                    p+=1
            else:
                while q<=s:
                    ans.append((1,nums2[q]))
                    q+=1
        ans=[j[1] for j in ans]
        return ans

if __name__=="__main__":
    s=Solution() 
    sample=[
        [[6,7],[6,0,4],  5],
        [[1,1,1,1],[1,1,1,1],3],
        [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            100
        ],
        [[6,7,5],[4,8,1], 3],
        [[3,9],[8,9],  3],
        
        [[3,4,6,5],[9,1,2,5,8,3],5]

        ]
    expected=[
        [6,7,6,0,4],
        [1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [8,7,5],
        [9,8,9],
        
        [9,8,6,5,3]
 
    ]
    for i in sample:
        print(s.maxNumber(i[0],i[1],i[2]))