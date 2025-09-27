class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This is a more optimal O(N^2) two-pointer approach.
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        n = len(nums)
        count = 0

        # Iterate from the end, fixing the longest side 'c' of a potential triangle.
        for i in range(n - 1, 1, -1):
            c = nums[i]
            left = 0
            right = i - 1

            # Use two pointers to find pairs (a, b) such that a + b > c.
            while left < right:
                a = nums[left]
                b = nums[right]

                if a + b > c:
                    # If nums[left] + nums[right] > c, then any element between
                    # left and right will also form a valid triangle with nums[right].
                    # For example, (nums[left+1], nums[right], c) is also valid.
                    # So, we count all these pairs at once.
                    count += right - left
                    
                    # Try a smaller second side to find more pairs.
                    right -= 1
                else:
                    # The sum is too small, so we need a larger first side.
                    left += 1
                    
        return count