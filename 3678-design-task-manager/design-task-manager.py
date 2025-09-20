import heapq

class TaskManager(object):
    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.dictTask = {}   # taskId -> [priority, userId]
        self.heap = []       # stores (-priority, -taskId)
        self.stale_count = 0 # number of stale heap entries

        for userId, taskId, priority in tasks:
            self.dictTask[taskId] = [priority, userId]
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId, taskId, priority):
        self.dictTask[taskId] = [priority, userId]
        heapq.heappush(self.heap, (-priority, -taskId))
        self.stale_count += 1
        if self.stale_count > len(self.heap) // 2:
            self._rebuild_heap()

    def edit(self, taskId, newPriority):
        if taskId in self.dictTask:
            self.dictTask[taskId][0] = newPriority
            heapq.heappush(self.heap, (-newPriority, -taskId))
            self.stale_count += 1
            if self.stale_count > len(self.heap) // 2:
                self._rebuild_heap()

    def rmv(self, taskId):
        if taskId in self.dictTask:
            self.dictTask[taskId][0] = -1
            self.stale_count += 1
            if self.stale_count > len(self.heap) // 2:
                self._rebuild_heap()

    def execTop(self):
        while self.heap:
            priority, neg_tid = heapq.heappop(self.heap)
            taskId = -neg_tid
            if taskId in self.dictTask and self.dictTask[taskId][0] == -priority:
                user = self.dictTask[taskId][1]
                self.dictTask[taskId][0] = -1
                return user
        return -1

    def _rebuild_heap(self):
        # Remove all stale entries and rebuild heap
        self.heap = [(-priority, -tid) for tid, (priority, _) in self.dictTask.items() if priority != -1]
        heapq.heapify(self.heap)
        self.stale_count = 0
