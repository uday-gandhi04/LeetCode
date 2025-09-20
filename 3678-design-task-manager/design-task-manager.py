class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.dictTask={}
        self.heap=[]

        for userId,taskId,priority in tasks:
            self.dictTask[taskId]=[priority,userId]       
            heapq.heappush(self.heap,(-priority,-taskId)) 

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.dictTask[taskId]=[priority,userId]
        heapq.heappush(self.heap,(-priority,-taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        self.dictTask[taskId][0]=newPriority
        heapq.heappush(self.heap,(-newPriority,-taskId))
        

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        del self.dictTask[taskId]
        

    def execTop(self):
        """
        :rtype: int
        """
        if not self.heap: 
            return -1
        out=heapq.heappop(self.heap)

        while -out[1] not in self.dictTask or -out[0]!=self.dictTask[-out[1]][0]:
            if not self.heap: 
                return -1
            out=heapq.heappop(self.heap)
        
        user=self.dictTask[-out[1]][1]
        del self.dictTask[-out[1]]
        
        return user
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()