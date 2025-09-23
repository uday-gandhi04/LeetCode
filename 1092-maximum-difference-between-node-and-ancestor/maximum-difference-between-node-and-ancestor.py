# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def helper(maxx,minn,root):

            if not root:
                return 
            
            maxDiff=0
            
            maxDiff=max(abs(maxx-root.val),abs(minn-root.val))
            
            maxx=max(maxx,root.val)
            minn=min(minn,root.val)
            
            leftmax=helper(maxx,minn,root.left)
            rightmax=helper(maxx,minn,root.right)

            
            return max(maxDiff,leftmax,rightmax)
        

        return helper(root.val,root.val,root)
        