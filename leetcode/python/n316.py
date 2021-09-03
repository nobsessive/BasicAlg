class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        v=list(s)
        d=dict()
        n=len(v)
        rep=[-1]*n
        # check repitition
        for i in range(n-1,-1,-1):
            if v[i] in d:
                rep[i]=1
            d[v[i]]=1
        # iterate through list v
        # for current index i, delete larger and repititive characters before it
        # if i not in stack, add it to stack else skip
        v.append('#')
        stack=[-1]
        in_stack=dict()
        for i in range(n):
            while v[stack[-1]]>=v[i]:
                if rep[stack[-1]]==1:
                    c=stack.pop()
                    del in_stack[v[c]]
                    v[c]='A' # mark as removed
                else:
                    break  
            if(v[i] not in in_stack):
                stack.append(i)
                in_stack[v[i]]=1
            else:
                v[i]='A'
        t=""
        for i in range(n):
            if v[i]!='A':
                t+=v[i]
        return t

if __name__=="__main__":
    s=Solution() 
    sample=[
        "abacb",
        "bcabc",
        "cbacdcbc"
        ]
    expected=[
        "abc",
        "abc",
        "acdb"
    ]
    for i in sample:
        print(s.removeDuplicateLetters(i))