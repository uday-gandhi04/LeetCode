class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def checkEven(nums):
            out=0

            for num in nums:
                if num^1==num+1:
                    out+=1
            return out
        
        def checkOdd(nums):
            out=0
            for num in nums:
                if num^1!=num+1:
                    out+=1
            return out

        def checkEvenOdd(nums):
            out=0
            odd=False

            for num in nums:
                if num^1==num+1 and not odd:
                    out+=1
                    odd=True
                elif num^1!=num+1 and odd:
                    out+=1
                    odd=False
            return out


        
        def checkOddEven(nums):
            out=0
            odd=False

            for num in nums:
                if num^1==num+1 and odd:
                    out+=1
                    odd=False
                elif num^1!=num+1 and not odd:
                    out+=1
                    odd=True
            return out

        return max(checkEven(nums),checkOdd(nums),checkEvenOdd(nums),checkOddEven(nums))