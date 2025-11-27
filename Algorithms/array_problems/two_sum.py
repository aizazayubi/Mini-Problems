# a leatcode solution
class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i

if __name__ == "__main__":
    nums = [11, 7, 11, 2]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))  # Output: [0, 1]