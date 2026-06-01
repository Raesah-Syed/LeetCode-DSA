# Last updated: 5/31/2026, 11:35:22 PM

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ps = 0
        pe = len(people) - 1
        boat = 0
        people.sort()
        
        # 1. Changed to <= so the last remaining person is counted
        while ps <= pe:
            # If they can share, move the left pointer forward
            if ps != pe and people[ps] + people[pe] <= limit:
                ps = ps + 1
            
            # The heaviest person (pe) ALWAYS gets a boat
            pe = pe - 1
            boat += 1
            
        # 2. Return the result for LeetCode compatibility
        return boat
