class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out=[]

        temp=[]

        for i in range(0,len(nums),3):
            temp.extend([nums[i],nums[i+1],nums[i+2]])
            if temp[-1]-temp[0]>k:
                return []
            out.append(temp)
            temp=[]
        
        for i in out:
            if i[-1]-i[0]>k:
                return []
        
        return out