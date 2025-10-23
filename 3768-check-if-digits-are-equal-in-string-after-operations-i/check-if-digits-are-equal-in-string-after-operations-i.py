class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr=list(int(s[i]) for i in range(len(s)))
        while len(arr)>2:
            for i in range(len(arr)-1):
                arr[i]=(arr[i]+arr[i+1])%10
            arr.pop(-1)
        
        return arr[0]==arr[1]
        