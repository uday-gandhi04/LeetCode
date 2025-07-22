class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        i=0
        j=0
        dic=set()
        out=0
        temp=0
        while j<n:
            if nums[j] not in dic:
                dic.add(nums[j])
                temp+=nums[j]
            else:
                out=max(temp,out)
                while i<j and nums[i]!=nums[j]:
                    dic.remove(nums[i])
                    temp-=nums[i]
                    i+=1
                i+=1
            j+=1
        
        return max(out,temp)
                



        