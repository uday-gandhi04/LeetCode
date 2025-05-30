class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        myset=set(nums)
        
        maxx=0
        temp=1

        

        for i in myset:
            if i-1 in myset:
                continue
            else:
                while(i+1 in myset):
                    temp+=1
                    i=i+1
                maxx=max(maxx,temp)
                temp=1
        
            
            
        return maxx
