class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target=0-nums[i]
            j=i+1
            k=len(nums)-1
            while j<k :
                if nums[j]+nums[k]==target :
                    
                    out.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
                elif(nums[j]+nums[k]>target):
                    k-=1
                else:
                    j+=1
        
        return out