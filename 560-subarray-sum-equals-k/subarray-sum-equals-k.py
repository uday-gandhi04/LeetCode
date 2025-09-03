class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        x=0
        dic=defaultdict(int)
        dic[0]+=1
        out=0
        for i,num in enumerate(nums):
            x+=num

            if x-k in dic:
                out+=dic[x-k]
            dic[x]+=1
        
        return out
            

        