class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        
        out = []
        heap = []

        # Push the first k-1 elements
        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        
        # Process the rest of the array
        for i in range(k - 1, len(nums)):
            # Push the current element
            heapq.heappush(heap, (-nums[i], i))
            
            # Remove elements outside the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            # The top of the heap is the max of the window
            out.append(-heap[0][0])
        
        return out
