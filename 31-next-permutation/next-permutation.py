class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        for i in range(n,0,-1):
            if nums[i-1]<nums[i]:
                p=nums[i-1]
                for j in range(n,i-1,-1):
                    if nums[j]>p:
                        nums[i-1],nums[j]=nums[j],nums[i-1]
                        break


                x=n
                j=i
                while j<=x:
                    nums[j],nums[x]=nums[x],nums[j]
                    j+=1
                    x-=1
                break
        else:
            x=n
            j=0
            while j<x:
                nums[j],nums[x]=nums[x],nums[j]
                j+=1
                x-=1
            

