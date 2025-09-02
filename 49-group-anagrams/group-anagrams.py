class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for s in strs:
            a=''.join(sorted(s))

            if a in dic:
                dic[a].append(s)
            else:
                dic[a]=[s]
        
        out=[]

        for values in dic.values():
            out.append(values)
        
        return out
