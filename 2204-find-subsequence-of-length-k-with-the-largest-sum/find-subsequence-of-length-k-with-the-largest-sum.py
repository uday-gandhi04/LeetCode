class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        heap=[]
        for idx,num in enumerate(nums):
            heapq.heappush(heap,(-num,idx))
        out=[float('inf')]*len(nums)
        x=[]
        for i in range(k):
            temp=heapq.heappop(heap)
            out[temp[1]]=-temp[0]
        for i in out:
            if i != float('inf'):
                x.append(i)
        return x
