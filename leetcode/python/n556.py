# p=cur+1
# while p<n and a[cur]<a[p]:
#     p+=1
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # turn n into a list of digits
        n_str = str(n)
        n_len = len(n_str)
        if n_len<2:
            return -1
        a=[]
        for i in range(n_len):
            a.append(int(n_str[i]))
        # find next larger digit for each element of a
        min=a[-1]
        cur=-1
        for i in range (n_len-2,-1,-1):
            if a[i]<a[i+1]:
                cur=i
                break
        if cur==-1:
            return -1
        # calculate the next larger number with exactly the same digits
        p=cur+1
        while (p<n_len and a[p]>a[cur]):
            p+=1
        # cur, p-1
        a[cur],a[p-1]=a[p-1],a[cur]
        a_tail=a[cur+1:n_len]
        a_tail.sort()
        a=a[:cur+1]+a_tail
        # now we have a[0-n-1] the next larger number
        # check if the next larger number is a 32-bit integer
        c=2147483647
        ans=0
        for i in range(n_len):
            ans=ans*10+a[i]
        if ans>c:
            return -1
        return ans

if __name__=="__main__":
    s=Solution()
    sample=[
        2147483476,
        12,
        21,
        230241
        
        ]
    ''' 
    expect=[
        2147483647
        21,
        -1,
        230421
        
        ]
    '''

    for i in sample:
        print(s.nextGreaterElement(i))