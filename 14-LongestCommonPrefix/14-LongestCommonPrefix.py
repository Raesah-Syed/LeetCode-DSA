# Last updated: 5/23/2026, 7:57:13 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 1. Use the first word as our master blueprint
        blueprint = strs[0]
        
        # 2. Loop through every character index of the blueprint
        for i in range(len(blueprint)):
            char_to_match = blueprint[i]
            
            # 3. Check this exact same index 'i' in all other words
            for other_word in strs[1:]:
                
                # CRITICAL SAFETY CHECKS:
                # Check A: Did we run out of letters in the other word? (i == len(other_word))
                # Check B: Does the letter at this column mismatch? (other_word[i] != char_to_match)
                if i == len(other_word) or other_word[i] != char_to_match:
                    
                    # Cut and return everything from index 0 up to (but excluding) 'i'
                    return blueprint[:i]
                
        # If we successfully finish the entire loop, the whole blueprint is the prefix
        return blueprint