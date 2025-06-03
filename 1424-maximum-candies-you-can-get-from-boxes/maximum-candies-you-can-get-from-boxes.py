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
        for i in range(n):
            if status[i]==1:
                keysFound.add(i)
        out=0
        while que:
            currBox=que.popleft()

            if currBox in visited:
                continue
            visited.add(currBox)

            box=containedBoxes[currBox]
            k=keys[currBox]

            for i in range(len(k)):
                keysFound.add(k[i])
            for i in range(len(box)):
                boxes.add(box[i])
            #print(currBox,keysFound,boxes)
            out+=candies[currBox]
            candies[currBox]=0

            for i in keysFound:
                if i in boxes:
                    que.append(i)

        return out

            




        