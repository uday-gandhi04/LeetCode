class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """

        visited=set()
        boxes=set()
        keysFound=set()
        que=deque()
        n=len(status)

        for i in range(len(initialBoxes)):
            if status[initialBoxes[i]]==1:
                que.append(initialBoxes[i])
            else:
                boxes.add(initialBoxes[i])

        out=0
        while que:
            currBox=que.popleft()

            if currBox in visited:
                continue
            visited.add(currBox)

            keysFound.update(keys[currBox])

            for c in containedBoxes[currBox]:
                if status[c]==1 or c in keysFound:
                    que.append(c)
                else:
                    boxes.add(c)
            out+=candies[currBox]

            openBox=boxes & keysFound
            que.extend(openBox)
            boxes-=openBox
            keysFound-=openBox

        return out

            




        