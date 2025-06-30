class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        out=0
        temp=0
        i=0
        j=1
        n=len(nums)
        while j<n:
            if nums[j]-nums[i]==1:
                temp=j-i+1
            elif nums[j]-nums[i]>1:
                while i+1<n and nums[i]==nums[i+1]:
                    i+=1
                i+=1
                j=i
                out=max(temp,out)
            j+=1
        return max(out,temp)

        