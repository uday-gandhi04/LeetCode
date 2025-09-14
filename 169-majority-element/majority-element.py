class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count=1
        x=nums[0]

        for num in nums[1:]:
            if num==x:
                count+=1
            else:
                if count:
                    count-=1
                else:
                    x=num
                    count=1
        
        return x




        