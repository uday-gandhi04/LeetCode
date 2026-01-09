# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def depth(root):
            if not root :
                return 0
            
            return max(depth(root.left),depth(root.right))+1
        
        d=depth(root)
        self.out=None
        def dfs(root,d):
            if not root:
                return 0
            
            l=dfs(root.left,d-1)
            r=dfs(root.right,d-1)
            if l==r and l==d-1:
                self.out=root
            
            return max(l,r)+1
        
        dfs(root,d)
        return self.out


            
            