import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Convert lists to numpy arrays
        arr1 = np.array(nums1)
        arr2 = np.array(nums2)
        
        # Merge and sort
        merged = np.sort(np.concatenate([arr1, arr2]))
        # Find median
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]   # Odd length
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2  # Even length