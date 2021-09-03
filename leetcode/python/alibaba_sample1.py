'''
Given two bit strings A and B, find the minimum number of operations required to convert A to B.
Operations are counted as follows:
    1. set A[i through j] = 1
    2. set A[i through j] = 0
where 0<=i<j<=len(A)
'''
class Solution:
    def solver(self,A, B):
        p,d=0,0
        n=len(A)
        set_break_flag=0
        clr_break_flag=0
        while p<n:
            if A[p]==B[p]:
                p+=1
                continue
            if A[p]==0: # advantage in set
                if set_break_flag==0:
                    d+=1
                else:
                    set_break_flag=0
                p+=1
                while p<n and (B[p]==1): # pass
                    p+=1
                while p<n and (A[p]==1 and B[p]==0): # break
                    p+=1
                    d+=1
                    set_break_flag=1
            else:       # advantage in clear
                if clr_break_flag==0:
                    d+=1
                else:
                    clr_break_flag=0
                p+=1
                while p<n and (B[p]==0): # pass
                    p+=1
                while p<n and (A[p]==0 and B[p]==1): # break
                    p+=1
                    d+=1
                    clr_break_flag=1
        return d

if __name__=="__main__":
    s=Solution() 
    sample=[
        [[1,0,1,0],[0,1,0,1]],
        [[1,1,1,1],[1,0,1,0]],
        [[0,0,0,0],[0,0,0,0]],
        [[1,0,0,1,1],[0,0,1,1,1]]
        ]
    expected=[
        3,
        2,
        0,
        2
    ]
    for i in sample:
        print(s.solver(i[0],i[1]))