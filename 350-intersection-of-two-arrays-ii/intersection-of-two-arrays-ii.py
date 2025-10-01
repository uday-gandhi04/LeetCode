class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2.sort()
        freq=Counter(nums2)
        out=[]

        for num in nums1:
            index = bisect_left(nums2, num)

            if index != len(nums2) and nums2[index] == num and freq[num]>0:
                freq[num]-=1
                out.append(num)
        return out



        