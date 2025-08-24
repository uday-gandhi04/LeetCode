class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=0
        j=0
        noZero=0
        out=0
        count=0

        while j <len(nums):
            if nums[j]==1:
                count+=1
            else:
                noZero+=1

                if noZero==1:
                    j+=1
                    continue
                out=max(out,count)

                while nums[i]!=0:
                    i+=1
                    count-=1     
                i+=1
                noZero-=1
            j+=1
        
        out=max(out,count)
        return out if noZero>0 else out-1
                

            