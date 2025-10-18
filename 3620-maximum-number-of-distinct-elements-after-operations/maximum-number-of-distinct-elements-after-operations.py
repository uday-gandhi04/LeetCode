class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()
        nextAvailable = float('-inf')
        count = 0

        for num in nums:
            left = num - k
            right = num + k
            assign = max(left, nextAvailable)

            if assign <= right:
                count += 1
                nextAvailable = assign + 1

        return count
