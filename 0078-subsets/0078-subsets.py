class Solution:
    def backtrack(self, i, temp, nums, ans):
        n = len(nums)

        if i >= n:
            # Current subset is complete
            ans.append(temp.copy())
            return

        # Choice 1: Include the current element
        temp.append(nums[i])
        self.backtrack(i + 1, temp, nums, ans)

        # Backtrack and remove the current element
        temp.pop()

        # Choice 2: Exclude the current element
        self.backtrack(i + 1, temp, nums, ans)

    def subsets(self, nums):
        ans = []
        temp = []

        # Start generating subsets from index 0
        self.backtrack(0, temp, nums, ans)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna