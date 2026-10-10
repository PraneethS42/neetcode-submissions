class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution, including sorting which is O(nlogn)
        nums.sort()
        ans = []
        for idx, num in enumerate(nums):
            # We want triplets that sum to 0, so if the first is 0 then rest are greater
            if num > 0:
                break

            # If the first value we choose is the same as the previous one it'll result in same triplet
            if idx > 0 and num == nums[idx-1]:
                continue

            # Now we redo Two Sum II, but don't return an ans, just add to res
            l, r = idx + 1, len(nums) - 1
            target = 0 - num
            while l < r:
                if nums[l] + nums[r] < target: # not big enough
                    l += 1
                elif nums[l] + nums[r] > target: # too big
                    r -= 1
                else:                             # just right
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # We need to make sure the next pair of two values that we find (if we do),
                    # isn't the same, so we shift until the left pointer is a diff value, ensuring that
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return ans

            


        