# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        out=[]
        def summ(root):
            
            if not root:
                return 0
            s=root.val+summ(root.left)+summ(root.right)
            out.append(s)
            return s
        
        total=summ(root)
        return max(x * (total - x) for x in out) % (10**9 + 7)

        