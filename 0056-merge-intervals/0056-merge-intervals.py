class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna