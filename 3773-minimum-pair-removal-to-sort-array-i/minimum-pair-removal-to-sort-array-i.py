class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def list_to_linkedlist(arr):
            dummy = ListNode()
            curr = dummy
            for x in arr:
                curr.next = ListNode(x)
                curr = curr.next
            return dummy.next
        
        head=list_to_linkedlist(nums)
        ptr=head
        i=head
        j=head
        out=0
        
        while True:

            isSorted=True
            h=head
            h_1=h.next

            while h_1:
                if h_1.val<h.val:
                    isSorted=False
                    break
                h=h_1
                h_1=h_1.next

            if isSorted:
                return out

            s=float('inf')
            ptr=head
            ptr1=head.next

            while ptr1:
                if ptr.val+ptr1.val<s:
                    s=ptr.val+ptr1.val
                    a=ptr
                    b=ptr1
                ptr=ptr1
                ptr1=ptr1.next
            
            a.val+=b.val
            a.next=b.next
            out+=1
        
        return out
