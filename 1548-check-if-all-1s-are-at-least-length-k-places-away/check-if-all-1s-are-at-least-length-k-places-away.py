class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = float('-inf')
        for i,bit in enumerate(nums):
            if bit:
                if i-prev-1<k:
                    return False
                prev=i
        
        return True