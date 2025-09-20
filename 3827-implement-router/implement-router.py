class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit=memoryLimit
        self.RouterQ=deque()
        self.setPackets=set()
        self.destinationSet=defaultdict(deque)


    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """

        if (source,destination,timestamp) in self.setPackets:
            return False
        
        
        

        if len(self.RouterQ)>=self.memoryLimit:
            p=self.RouterQ.popleft()
            self.destinationSet[p[1]].popleft()
            self.setPackets.remove(p)
        
        self.RouterQ.append((source,destination,timestamp))
        self.setPackets.add((source,destination,timestamp))
        self.destinationSet[destination].append((source,destination,timestamp))

        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if self.RouterQ:
            p=self.RouterQ.popleft()
            self.destinationSet[p[1]].popleft()
            self.setPackets.remove(p)

            return p
        else:
            return []
        
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        arr = self.destinationSet[destination]
        n = len(arr)

        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if arr[mid][2] < startTime:
                l = mid + 1
            else:
                r = mid
        leftEnd = l

        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if arr[mid][2] <= endTime:
                l = mid + 1
            else:
                r = mid
        rightEnd = l
        
        return rightEnd-leftEnd



        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)