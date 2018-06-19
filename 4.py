class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = list()

        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i +=1
            elif nums1[i] == nums2[j]:
                merge.append(nums1[i])
                merge.append(nums2[j])
                i += 1
                j += 1
            else:
                merge.append(nums2[j])
                j += 1
        if i < len(nums1):
            for k in range(i, len(nums1)):
                merge.append(nums1[k])
        if j < len(nums2):
            for k in range(j, len(nums2)):
                merge.append(nums2[k])
        
        if len(merge) % 2 == 1:
            return merge[(int)((len(merge) - 1) / 2)]
        else:
            return (merge[(int)(len(merge) / 2)] + merge[int(len(merge) / 2 - 1)]) / 2

s = Solution()

print(s.findMedianSortedArrays([1],[2,3]))