class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Step 1: Find potential candidates
        a, b, c1, c2 = 0, 1, 0, 0  # initialize with different values
        for num in nums:
            if num == a:
                c1 += 1
            elif num == b:
                c2 += 1
            elif c1 == 0:
                a, c1 = num, 1
            elif c2 == 0:
                b, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        
        # Step 2: Verify candidates
        c1 = c2 = 0
        for num in nums:
            if num == a:
                c1 += 1
            elif num == b:
                c2 += 1
        
        result = []
        n = len(nums)
        if c1 > n // 3:
            result.append(a)
        if c2 > n // 3:
            result.append(b)
        
        return result
