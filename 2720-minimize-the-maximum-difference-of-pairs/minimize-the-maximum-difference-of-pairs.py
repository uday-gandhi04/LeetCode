class Solution:
    def minimizeMax(self, nums, p):
        nums = sorted(nums)
        n = len(nums)
        r = (nums[-1] - nums[0])
        l = 0

        while(l < r):
            mid = (l+r)//2
            curr = 0
            i = 1
            while i < n:
                if nums[i]-nums[i-1] <= mid:
                    curr += 1
                    i += 1     
                i += 1
            if curr >= p:
                r = mid
            else:
                l = mid + 1

        return l