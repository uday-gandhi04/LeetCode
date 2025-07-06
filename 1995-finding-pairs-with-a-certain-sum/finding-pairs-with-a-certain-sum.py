class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1=nums1
        self.nums2=nums2
        self.dic_nums1={}
        self.dic_nums2={}

        """for i,num in enumerate(nums1):
            if num in self.dic_nums1:
                self.dic_nums1[num]=[i]
            else:
                self.dic_nums1[num].append(i)"""
            
        for i,num in enumerate(nums2):
            if num in self.dic_nums2:
                self.dic_nums2[num].append(i)     
            else:
                self.dic_nums2[num]=[i]

    def add(self, ix, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.dic_nums2[self.nums2[ix]].pop(self.dic_nums2[self.nums2[ix]].index(ix))
        if not self.dic_nums2[self.nums2[ix]]:
            self.dic_nums2.pop(self.nums2[ix])

        self.nums2[ix]+=val
        if self.nums2[ix] in self.dic_nums2:
            self.dic_nums2[self.nums2[ix]].append(ix)
        else:
            self.dic_nums2[self.nums2[ix]]=[ix]

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        out=0
        for num in self.nums1:
            target=tot-num

            if target in self.dic_nums2:
                out+=len(self.dic_nums2[target])
        return out

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)