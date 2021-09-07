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
    # construct binary tree from list nums[]
    # nodes in nums are arranged one level by one level i.e. level 0 (root), level 1, ...
    # only necessary 'null' nodes are included in the list
    # child_dir is the direction of the child node, left=0, right=1
    def construct_binary_tree2(self, nums, child_dir=0,child_cur=[], parent_queue=[]):
        n=len(nums)
        if child_cur==n or nums==[]:
            return None
        if parent_queue==[] or parent_queue==None: # if parent_queue is empty, it means this is the root node
            root=TreeNode(nums[0])
            child_cur=1
            parent_queue=[root]
            self.construct_binary_tree2(nums,0,child_cur,parent_queue)
            return root
        if child_dir==0:
            if nums[child_cur]!='null':
                parent_queue[0].left=TreeNode(nums[child_cur])
                parent_queue.append(parent_queue[0].left)
            child_cur+=1
            self.construct_binary_tree2(nums,1,child_cur,parent_queue)
        else:
            if nums[child_cur]!='null':
                parent_queue[0].right=TreeNode(nums[child_cur])
                parent_queue.append(parent_queue[0].right)
            parent_queue.pop(0)
            child_cur+=1
            self.construct_binary_tree2(nums,0,child_cur,parent_queue)
        return
    # construct binary tree from list nums[]
    # nodes in nums are arranged one level by one level i.e. level 0 (root), level 1, ...
    # each node is included even it is a null node
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
        pre=s.construct_binary_tree2(item)

        c=s.inorderTraversal(pre)
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)