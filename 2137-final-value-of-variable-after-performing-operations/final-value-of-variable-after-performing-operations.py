class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X=0

        for op in operations:
            if op[0]=='+' or op[-1]=='+':
                X+=1
            else:
                X-=1
        return X
        