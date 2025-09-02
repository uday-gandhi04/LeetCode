"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        
        visited={}

        q=deque()

        q.append(node)
        visited[node.val]=Node(node.val)

        while q:
            no=q.popleft()

            for n in no.neighbors:
                if n.val not in visited:
                    q.append(n)
                    visited[n.val]=Node(n.val)
                visited[no.val].neighbors.append(visited[n.val])
        
        return visited[node.val]


                                                                                                                                                 
        

        