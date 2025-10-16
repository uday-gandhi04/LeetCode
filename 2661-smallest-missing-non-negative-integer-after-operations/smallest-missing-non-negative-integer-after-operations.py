from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # Count occurrences of each remainder mod value
        count = Counter(num % value for num in nums)
        
        # Try numbers starting from 0 upward
        m = 0
        while True:
            r = m % value
            if count[r] > 0:
                count[r] -= 1
            else:
                return m
            m += 1
        