class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = [0]*(n+m)
        i,j,k = 0,0,0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                c[k] = nums1[i]
                k += 1
                i += 1
            else:
                c[k] = nums2[j]
                k += 1
                j += 1
        
        while i<m:
            c[k] = nums1[i]
            k += 1
            i += 1
        
        while j<n:
            c[k] = nums2[j]
            k += 1
            j += 1

        for l in range(n+m):
            nums1[l] = c[l]