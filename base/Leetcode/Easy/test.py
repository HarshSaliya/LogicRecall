class Solution:
    def merge(self, nums1, m, nums2, n):
        # Step 1: nums1 ke placeholder zeros ki jagah nums2 ke elements daalo
        nums1[m:] = nums2[:n]

        # Step 2: ab poori nums1 ko sort karo (tumhara wala loop)
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if nums1[i] < nums1[j]:
                    nums1[j], nums1[i] = nums1[i], nums1[j]

        # return kuch nahi karna - in-place modify karna hai