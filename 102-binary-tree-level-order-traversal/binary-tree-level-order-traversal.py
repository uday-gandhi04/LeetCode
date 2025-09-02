# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        out=[]

        bfs=[root]

        out=[[root.val]]

        while bfs:

            level=[]
            levelval=[]
            n=len(bfs)
            for i in range(n):
                node=bfs.pop(0)
                if node.left:
                    level.append(node.left)
                    levelval.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    levelval.append(node.right.val)
            bfs=level
            if levelval:
                out.append(levelval)
        
                
        return out

        