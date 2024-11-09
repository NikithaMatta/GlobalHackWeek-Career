# Problem Implementation
def first_non_repeating_character(s: str) -> int:
    # Step 1: Count the occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find the first character with count 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index  # Return the index of the first non-repeating character

    return -1  # Return -1 if all characters repeat

# Test cases
print(first_non_repeating_character("simplilearn"))  # Output: 0 (since 's' is the first non-repeating)
print(first_non_repeating_character("aabbcc"))       # Output: -1 (no non-repeating character)
print(first_non_repeating_character("globalhackweek"))      # Output: 2 (since 'l' is the first non-repeating)
