class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        hashmap=set()

        for num in arr1:
            s=str(num)
            for i in range(1,len(s)+1):
                hashmap.add(s[:i])
        out=''
        for num in arr2:
            s=str(num)
            for i in range(1,len(s)+1):
                temp=s[:i]
                if temp in hashmap:
                    out=temp if len(temp)>len(out) else out

        return(len(out))