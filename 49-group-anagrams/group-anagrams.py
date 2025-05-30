class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic={}

        for i in strs:
            s=tuple(sorted(i))
            if s not in dic:
                dic[s]=[]
            dic[s].append(i)
        
        return list(dic.values())

        
