# Last updated: 5/18/2026, 7:23:39 PM
# use first word and length to traverse
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return ""
5        
6        # 1. Use the first word as our master blueprint
7        blueprint = strs[0]
8        
9        # 2. Loop through every character index of the blueprint
10        for i in range(len(blueprint)):
11            char_to_match = blueprint[i]
12            
13            # 3. Check this exact same index 'i' in all other words
14            for other_word in strs[1:]:
15                
16                # CRITICAL SAFETY CHECKS:
17                # Check A: Did we run out of letters in the other word? (i == len(other_word))
18                # Check B: Does the letter at this column mismatch? (other_word[i] != char_to_match)
19                if i == len(other_word) or other_word[i] != char_to_match:
20                    
21                    # Cut and return everything from index 0 up to (but excluding) 'i'
22                    return blueprint[:i]
23                
24        # If we successfully finish the entire loop, the whole blueprint is the prefix
25        return blueprint