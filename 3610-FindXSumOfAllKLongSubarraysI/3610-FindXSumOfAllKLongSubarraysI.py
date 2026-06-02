# Last updated: 6/1/2026, 10:50:47 PM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import Counter
        
        # 1. Initialize count for the first window
        counts = Counter(nums[:k])
        res = []
        
        def calculate_x_sum(d, x):
            # Sort only the unique elements currently in the window
            # Sort by frequency (desc), then by value (desc)
            sorted_items = sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # Sum the top x
            current_sum = 0
            for i in range(min(x, len(sorted_items))):
                val, freq = sorted_items[i]
                current_sum += (val * freq)
            return current_sum

        # 2. Add the result for the first window
        res.append(calculate_x_sum(counts, x))
        
        # 3. Slide the window one step at a time
        for i in range(k, len(nums)):
            # Incoming element
            counts[nums[i]] += 1
            # Outgoing element
            counts[nums[i - k]] -= 1
            
            # Clean up the dictionary if a count hits 0
            if counts[nums[i - k]] == 0:
                del counts[nums[i - k]]
            
            # Calculate sum for this new window
            res.append(calculate_x_sum(counts, x))
            
        return res