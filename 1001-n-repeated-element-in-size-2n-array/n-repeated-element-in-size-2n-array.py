class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums[0]==nums[1] or nums [0]==nums[2]:
            return nums[0]
        if nums[1]==nums[2]:
            return nums[1]

        out=nums[3]
        freq=1

        for num in nums[4:]:
            if freq==0:
                out=num
                freq+=1
            elif out!=num:
                freq-=1
            else:
                freq+=1
        
        return out
