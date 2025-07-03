class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out=0
        summ=sum(nums)
        n=len(nums)
        while summ>0:
            flag=True
            for i in range(n):
                if nums[i]%2!=0:
                    flag=False
                    nums[i]-=1
                    out+=1
                    summ-=1
            if flag:
                for i in range(n):
                    summ=summ-(nums[i]/2)
                    nums[i]/=2
                out+=1
        return out
            

