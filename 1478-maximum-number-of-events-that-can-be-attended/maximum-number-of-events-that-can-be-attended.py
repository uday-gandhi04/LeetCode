class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events = sorted(events, key = lambda x: (x[0], x[1]))
        curr_day = events[0][0]
        event_id = 0
        event_cnt = 0
        h = []
        while event_id < len(events):
            if curr_day >= events[event_id][0]:
                heappush(h, (events[event_id][1], event_id))
                event_id += 1
            else:
                if h:
                    event_end, x = heappop(h)
                    if curr_day <= event_end:
                        event_cnt += 1
                        curr_day += 1
                else:
                    curr_day = events[event_id][0]
        while h: 
            event_end, x = heappop(h)
            if curr_day <= event_end:
                event_cnt += 1
                curr_day += 1

            
        return event_cnt         