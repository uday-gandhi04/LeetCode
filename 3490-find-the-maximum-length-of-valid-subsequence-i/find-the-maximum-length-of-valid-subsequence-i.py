class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """def checkEven(nums):
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
            return out"""
        

        checkEven=0
        checkOdd=0
        checkEvenOdd=0
        checkOddEven=0
        even1=True
        odd2=True
        for num in nums:
            
            if num^1==num+1:
                checkEven+=1
                if even1:
                    checkEvenOdd+=1
                    even1=False
                if not odd2:
                    checkOddEven+=1
                    odd2=True
            else:
                checkOdd+=1
                if not even1:
                    checkEvenOdd+=1
                    even1=True
                if odd2:
                    checkOddEven+=1
                    odd2=False


        return max(checkEven,checkOdd,checkEvenOdd,checkOddEven)