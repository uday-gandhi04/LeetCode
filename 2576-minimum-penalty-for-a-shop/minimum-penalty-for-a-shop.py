class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        count_y=customers.count('Y')
        count_n=customers.count('N')
        penalty=count_y
        minn=count_y
        idx=0

        for i,ch in enumerate(customers):
            if ch=='Y':
                penalty-=1
            else:
                penalty+=1

            if penalty<minn:
                idx=i+1
                minn=penalty
        return idx
                
        