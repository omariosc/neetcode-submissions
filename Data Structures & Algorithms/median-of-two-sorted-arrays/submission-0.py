class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        A, B = nums1, nums2

        # Binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2      # partition index in A
            j = half - i - 2      # partition index in B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Aleft is too big, move A partition left
            elif Aleft > Bright:
                r = i - 1

            # Bleft is too big, move A partition right
            else:
                l = i + 1