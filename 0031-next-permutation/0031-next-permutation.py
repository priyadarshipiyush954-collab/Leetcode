class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the breakpoint
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # Step 2 & 3: Find the next slightly larger number and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 4: Reverse the right half
        nums[i + 1:] = reversed(nums[i + 1:])
        