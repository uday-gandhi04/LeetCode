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

        def helper(arr,root):

            if not root:
                return 
            
            maxDiff=0
            if arr:
                for i in arr:
                    maxDiff=max(maxDiff,abs(i-root.val))
            
            arr.append(root.val)
            
            leftmax=helper(arr[:],root.left)
            rightmax=helper(arr[:],root.right)

            
            return max(maxDiff,leftmax,rightmax)
        

        return helper([],root)
        