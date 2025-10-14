class Solution(object):
    def hasIncreasingSubarrays(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window=2*k
        n=len(arr)
        for i in range(n-window+1):
            a=False
            count=1
            for j in range(i+1,i+window):
                if arr[j]>arr[j-1]:
                    count+=1
                elif count>=k:
                    count=1
                else:
                    break
            if count==k or count==2*k:
                return True
        return False
