class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total=sum(apple)

        capacity.sort(reverse=True)

        count=0
        
        for c in capacity:
            if total<=0:
                return count
            
            total-=c
            count+=1
        return count