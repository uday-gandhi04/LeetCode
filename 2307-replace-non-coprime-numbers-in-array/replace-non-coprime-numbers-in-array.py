class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]

        def findGCD(a,b):
            while b != 0:
                # How can you update a and b using the remainder?
                # A neat trick in Python is swapping them in one line.
                a, b = b, a % b
            
            return a


        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                num1 = stack.pop()
                num2 = stack.pop()
                gcd = findGCD(num1, num2)
                if gcd>1:
                    lcm = (num1 * num2) // gcd
                    stack.append(lcm)
                else: 
                    stack.append(num2)
                    stack.append(num1)
                    break

        return stack
