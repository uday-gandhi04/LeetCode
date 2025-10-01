class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        out=0
        prefixSum=0
        for i in range(len(nums)-1):
            prefixSum+=nums[i]
            total-=nums[i]

            if not (prefixSum - total)%2:
                out+=1
        
        return out
            