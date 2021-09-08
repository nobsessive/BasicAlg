# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numTrees(self, n: int):
        if n==1:
            return 1
        ret=[1,1] # Catalan number
        for k in range(2,n+1):
            ret_k=0
            for i in range(k):
                ret_k+=ret[i]*ret[k-i-1]
            ret.append(ret_k)
        return ret[n]
    
if __name__=="__main__": 
    s=Solution() 
    sample=[
        3,
        1,
        4
    ]
    expected=[
        5,
        1,
        14
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.numTrees(item)
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)