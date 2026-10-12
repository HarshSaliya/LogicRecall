class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result  = []
        for i in nums2:
            if i in nums1 and i not in result:
                result.append(i)

        
        return result
