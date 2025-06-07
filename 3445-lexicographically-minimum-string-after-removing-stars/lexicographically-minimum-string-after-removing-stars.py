class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap=[]
        n=len(s)
        
        for i in range(n):
            if s[i]=='*':
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,(s[i],-i))

        arr=[]
        while heap:
            x=heapq.heappop(heap)
            arr.append((x[0],-x[1]))

        arr=sorted(arr,key=lambda x:x[1])

        return "".join(c[0] for c in arr)