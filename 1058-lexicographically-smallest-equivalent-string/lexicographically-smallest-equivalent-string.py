class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        arr=[]
        dic={}
        n=len(s1)

        for i in range(n):
            temp=[]
            if s1[i] in dic and s2[i] in dic:
                if dic[s1[i]] != dic[s2[i]]:
                    g1 = dic[s1[i]]
                    g2 = dic[s2[i]]
                    if g2<g1:
                        g1,g2=g2,g1
                    
                    arr[g1].update(arr[g2])

                    for key, value in list(dic.items()):
                        if value == g2:
                            dic[key] = g1             
            elif s1[i]in dic:
                arr[dic[s1[i]]].update((s1[i],s2[i]))
                dic[s2[i]]=dic[s1[i]]
            elif s2[i] in dic:
                arr[dic[s2[i]]].update((s1[i],s2[i]))
                dic[s1[i]]=dic[s2[i]]
            else:
                arr.append(set([s1[i],s2[i]]))
                dic[s1[i]]=len(arr)-1
                dic[s2[i]]=len(arr)-1
        output_chars = []
        for ch in baseStr:
            if ch in dic:
                grp = arr[dic[ch]]
                output_chars.append(min(grp))
            else:
                output_chars.append(ch)

        return "".join(output_chars)
        
        