class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2 

        l, r = 0, len(A) - 1

        while True:
            m = (l + r) // 2
            b = half - m - 2

            A1 = A[m] if m >= 0 else float("-infinity")
            A2 = A[m + 1] if (m + 1) < len(A) else float("infinity")

            B1 = B[b] if b >= 0 else float("-infinity")
            B2 = B[b + 1] if (b + 1) < len(B) else float("infinity")

            if A1 <= B2 and B1 <= A2:
                if total % 2:
                    return min(A2, B2)
                else:
                    return (max(A1, B1) + min(A2, B2)) / 2
                
            elif A1 > B2:
                r = m - 1

            else:
                l = m + 1