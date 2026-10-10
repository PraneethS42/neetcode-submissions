class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution, including sorting which is O(nlogn) <- have this privilege now
        nums.sort()
        res = []
        for idx, n in enumerate(nums):
            if n > 0: # Can't add to 0 if all of following are >0
                break

            if idx > 0 and n == nums[idx-1]: #skip if same as previous
                continue

            lp = idx+1
            rp = len(nums)-1
            target = 0-n

            while lp < rp:
                if nums[lp]+nums[rp] == target:
                    res.append([n, nums[lp], nums[rp]])
                    # We're not done, can extract mulitple pairs
                    lp += 1
                    rp -= 1
                    # Shift the until left ptr is diff to ensure no duplicate
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1

                elif nums[lp] + nums[rp] < target:
                    lp += 1
                else:
                    rp -=1
        
        return res

            


        