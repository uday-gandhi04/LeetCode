# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        q=deque()

        out=1
        Sum=root.val
        level=1

        q.append(root)
        
        while q:
            temp=[]
            tempSum=0
            level+=1
            flag=False
            for node in q:    
                l=node.left
                r=node.right
                
                if l:
                    temp.append(l)
                    tempSum+=l.val
                    flag=True
                if r:
                    temp.append(r)
                    tempSum+=r.val
                    flag=True
            
            q=temp[:]
            if tempSum>Sum and flag:
                out=level
                Sum=tempSum
        
        return out

                

                