# Last updated: 5/17/2026, 3:56:17 PM
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Group into buckets
            c = [0, 0, 0]
            for s in stones:
                c[s % 3] += 1

            # Branch 1: Even zeros (No turn switching)
            if c[0] % 2 == 0:
                return min(c[1], c[2]) > 0 # Alice just needs choices to win

            # Branch 2: Odd zeros (Bob switches turns)
            return abs(c[1] - c[2]) > 2 # Alice needs a massive backup supply to win