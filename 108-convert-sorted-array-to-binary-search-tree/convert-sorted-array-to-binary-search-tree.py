# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def bst(nums):
            if not nums:
                return 
            
            n=len(nums)

            if n==1:
                return TreeNode(nums[0])

            node=TreeNode(nums[n//2])

            l=bst(nums[:n//2])
            r=bst(nums[(n//2)+1:])

            node.left=l
            node.right=r

            return node
        
        return bst(nums)
