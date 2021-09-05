'''
    remove k digits is equivalent to keep n-k digits
    use increasing monotonic stack to solve the problem
    This is a sub-question of n321.py
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        t=n-k
        s=[]
        cnt=0   
        for i in range(n):
            while s and cnt+n-i>t and num[s[-1]] > num[i]:
                s.pop()
                cnt -= 1
            if cnt<t:
                s.append(i)
                cnt += 1
        ans=''
        while s:
            if num[s[0]]=='0':
                s.pop(0)
            else:
                break
        while s:
            ans+=num[s.pop(0)]
        if ans=='':
            ans='0'
        return ans
if __name__=="__main__":
    s=Solution() 
    sample=[
        ["1432219",3],
        ["10200",1],
        ["10",2],
        ]
    expected=[
        "1219",
        "200",
        "0"
 
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.removeKdigits(item[0],item[1])
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)
