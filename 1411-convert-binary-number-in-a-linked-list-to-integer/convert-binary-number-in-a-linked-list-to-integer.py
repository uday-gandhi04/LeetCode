# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        B=[]
        def traverse(node):
            if not node:
                return 
            B.append(node.val)
            traverse(node.next)
        
        traverse(head)
        return int(''.join(map(str, B)), 2)

