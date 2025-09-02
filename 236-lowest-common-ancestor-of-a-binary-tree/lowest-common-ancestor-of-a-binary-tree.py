# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        out=None
        def find(root):

            if not root: 
                return
            
            if root==p or root==q:
                return root
            
            a=find(root.left)
            b=find(root.right)

            if a and b:
                return root
            elif a :
                return a
            return b
        
        return find(root)
            
            
            

            
            

             


            
            