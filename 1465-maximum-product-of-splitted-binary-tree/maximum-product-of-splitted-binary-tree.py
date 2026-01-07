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

        out=[0]
        total=[0]

        def summ(root):
            
            if not root:
                return 0
            return root.val+summ(root.left)+summ(root.right)
        
        total[0]=summ(root)
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)

            out[0]=max(out[0],(total[0]-left)*left)

            right=dfs(root.right)

            out[0]=max(out[0],(total[0]-right)*right)

            return left+root.val+right

        dfs(root)

        return out[0]%(10**9 + 7)


        