# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=[0]
        def helper(r):

            if not r:
                return [0,0]
            
            leftSum,leftCount=helper(r.left)
            rightSum,rightCount=helper(r.right)

            total=r.val+leftSum+rightSum
            x = total/(1+leftCount+rightCount)
            if x == r.val:
                count[0]+=1
            
            return total,1+leftCount+rightCount
        helper(root)
        return count[0]

