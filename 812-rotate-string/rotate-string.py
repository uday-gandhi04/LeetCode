class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s)!=len(goal):
            return False
        s=deque(list(s))
        goal=deque(list(goal))
        n=len(s)
        for _ in range(n):
            if s == goal:
                return True
            
            ch=s.popleft()
            s.append(ch)
        
        return False




