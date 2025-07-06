class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1=nums1
        self.nums2=nums2
        self.cach1={}
        self.cach2={}

        for num in nums1:
            if num not in self.cach1:
                self.cach1[num]=0
            self.cach1[num]+=1
        
        for num in nums2:
            if num not in self.cach2:
                self.cach2[num]=0
            self.cach2[num]+=1
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        value=self.nums2[index]
        self.cach2[value]-=1

        if self.cach2[value]==0:
            del self.cach2[value]

        new=val+value
        self.nums2[index]=new
        if new not in self.cach2:
            self.cach2[new]=1
        else:
            self.cach2[new]+=1
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res=0
        for key in self.cach1:
            if tot-key in self.cach2:
                val=tot-key
                res+= self.cach1[key] * self.cach2[val]
        
        return res

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)