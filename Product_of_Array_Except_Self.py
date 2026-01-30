from typing import List


class Solution:
    """LeetCode 238 - Product of Array Except Self

    Time complexity: O(n)
    Space complexity: O(1) extra space (output array not counted)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # result array holds prefix products first
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # multiply by suffix products in a single pass from the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [1, 2, 3, 4]
    print("Input:", nums1)
    print("Output:", s.productExceptSelf(nums1))  # [24, 12, 8, 6]

    # Example 2
    nums2 = [-1, 1, 0, -3, 3]
    print("Input:", nums2)
    print("Output:", s.productExceptSelf(nums2))  # [0, 0, 9, 0, 0]
