from typing import List


class Solution:
    """LeetCode 4 - Median of Two Sorted Arrays

    Time complexity: O(log(min(m, n)))
    Space complexity: O(1)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    print("Input:", nums1, nums2)
    print("Output:", s.findMedianSortedArrays(nums1, nums2))  # 2.0

    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Input:", nums1, nums2)
    print("Output:", s.findMedianSortedArrays(nums1, nums2))  # 2.5

    # Additional tests
    print(s.findMedianSortedArrays([], [1]))  # 1.0
    print(s.findMedianSortedArrays([2], []))  # 2.0
    print(s.findMedianSortedArrays([0, 0], [0, 0]))  # 0.0
