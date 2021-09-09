# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        pass
    def print_tree(self, root, node_list):
        if(root == None):
            node_list.append('null')
            return
        node_list.append(root.val)
        self.print_tree(root.left, node_list)
        self.print_tree(root.right, node_list)  
if __name__=="__main__": 
    s=Solution() 
    sample=[
        1
        ]
    expected=[
        []
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.generateTrees(item)
        u=[]
        for k in c:
            t=[]
            s.print_tree(k,t)
            u.append(t)
        print(u)