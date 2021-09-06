# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root==None or root==[]:
            return []
        def inorder(node,s):
            if node==None:
                s.append('null')
                return
            # if left exists, visit left
            if node.left!=None:
                inorder(node.left,s)
            # visit node itself
            s.append(node.val)
            # if right exists, visit right
            if node.right!=None:
                inorder(node.right,s)
        s=[]
        inorder(root,s)
        return s
    def construct_binary_tree(self, nums):
        def insert(nums,cur):
            if cur>=len(nums) or nums[cur]=='null':
                return None
            root=TreeNode(nums[cur])
            root.left=insert(nums,cur*2+1)
            root.right=insert(nums,cur*2+2)
            return root
        if len(nums)==0:
            return None
        root=insert(nums,0)
        return root

if __name__=="__main__": 
    s=Solution() 
    sample=[
        [1,'null',2,3],
        [],
        [1],
        [1,2],
        [1,'null',2]
        ]
    expected=[
        [1,3,2],
        [],
        [1],
        [2,1],
        [1,2]
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        pre=s.construct_binary_tree(item)

        c=s.inorderTraversal(pre)
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)