class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        out=0
        for fruit in fruits:
            flag=False
            for i in range(len(baskets)):
                if baskets[i]>=fruit:
                    baskets[i]=0
                    flag=True
                    break
            if not flag:
                out+=1
        return out

        