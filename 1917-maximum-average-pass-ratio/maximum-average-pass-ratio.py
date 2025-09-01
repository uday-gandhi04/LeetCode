class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq

        heap=[]

        for c in classes:
            pi=float(c[0])
            ti=float(c[1])

            gain=((pi+1)/(ti+1))-(pi/ti)
            heap.append((-gain,pi,ti))

        heapq.heapify(heap)
        
        for s in range(extraStudents):
            c=heapq.heappop(heap)
            pi=float(c[1])+1
            ti=float(c[2])+1
            gain=((pi+1)/(ti+1))-(pi/ti)

            heapq.heappush(heap,(-gain,pi,ti))
        
        out=0.0
        for c in heap:
            out+=c[1]/c[2]
        
        return out/len(heap)





        