class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        The problem asks you to find the maximum possible
        sum of any subarray (a continuous part of the array)
        with the additional condition that the length
         of that subarray must be divisible by k.
         You can pick any starting and ending positions as long
         as the number of elements in that segment is a multiple
         of k. Among all such valid subarrays, you must return
         the one with the highest sum.
         The challenge is to compute this efficiently even for very large arrays.
        """

        prefix = 0
        INF = float('inf')

        # smallest prefix sum for each (index % k)
        best_min = [INF] * k
        best_min[0] = 0

        ans = -10**30
        idx = 0  # prefix index

        for x in nums:
            idx += 1
            prefix += x
            r = idx % k

            # Try forming a valid subarray ending here
            ans = max(ans, prefix - best_min[r])

            # Update smallest prefix sum for this remainder class
            best_min[r] = min(best_min[r], prefix)

        return ans


# --------- Example Usage ----------
s = Solution()
print(s.maxSubarraySum([1,2], 1))                    # 3
print(s.maxSubarraySum([-1,-2,-3,-4,-5], 4))         # -10
print(s.maxSubarraySum([-5,1,2,-3,4], 2))            # 4
