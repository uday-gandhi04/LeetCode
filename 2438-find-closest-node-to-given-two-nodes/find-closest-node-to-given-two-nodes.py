class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """

        minNode1=[float('inf')]*len(edges)
        minNode2=[float('inf')]*len(edges)

        def bfs(node,arr):
            queue=deque()
            queue.append(node)
            dist=0

            visited=set()

            while queue:
                n=queue.popleft()
                if n in visited:
                    break
                visited.add(n)
                arr[n]=dist
                dist+=1
                if edges[n]!=-1:
                    queue.append(edges[n])
        
        bfs(node1,minNode1)
        bfs(node2,minNode2)

        out=float('inf')
        temp=out
        idx=-1

        for i in range(len(edges)):
            temp=min(out,max(minNode1[i],minNode2[i]))
            if temp!=out:
                idx=i
            out=temp
        return idx




        