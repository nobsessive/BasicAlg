# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        def insert(root, value):
            if root is None:
                return TreeNode(value)
            if value>root.val:
                p=root
                root=TreeNode(value)
                root.left=p    
            else:
                root.right=insert(root.right, value)
            return root
        def bfs(s,ans):
            while s !=[]:
                if s[0]=='null':
                    ans.append('null')
                    s.pop(0)
                    return
                ans.append(s[0].val)
                s.append('null' if s[0].left==None else s[0].left)
                s.append('null' if s[0].right==None else s[0].right)
                s.pop(0)
                bfs(s,ans)

        n=len(nums)
        root=TreeNode(nums[0])
        for i in range(1,n):
            root=insert(root,nums[i])
        return root
        ## follows is for testing purpose: return the binary tree as a list
        # ans=[]
        # s=[root]
        # bfs(s,ans)
        # while ans[-1]=='null':
        #     ans.pop()
        # return ans
if __name__=="__main__": 
    s=Solution() 
    sample=[
        [3,2,1,6,0,5],
        [3,2,1]
        ]
    expected=[
        [6,3,5,'null',2,0,'null','null',1],
        [3,'null',2,'null',1]
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.constructMaximumBinaryTree(item)
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)