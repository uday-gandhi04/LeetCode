# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(root,val):
            if not root:
                return True
            if root.val!=val:
                return False
            return check (root.right,val) and check(root.left,val)
        return check(root,root.val)
        