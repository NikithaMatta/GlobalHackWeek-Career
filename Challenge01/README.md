# Challenge One: Solve a Common Coding Interview Probelm 

## Problem Statement

**First Non-Repeating Character in a String**

Given a string, identify the first non-repeating character and return its index. If every character in the string repeats, return `-1`.

**Example:**
- Input: `"globalhackweek"`
- Output: `2` (since `'l'` is the first non-repeating character)

## Approach
1. **Character Counting:** We use a dictionary to store the frequency of each character in the string.
2. **Index Traversal:** We traverse the string a second time to find the index of the first character with a frequency of 1.

### Complexity Analysis
- **Time Complexity:** `O(n)` - two passes over the string, where `n` is the length of the string.
- **Space Complexity:** `O(k)` - where `k` is the number of unique characters in the string.

## Solution Code

```python
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
```

## Example Usage

```python
# Example Input and Expected Output
print(first_non_repeating_character("globalhackweek"))  # Expected Output: 2
print(first_non_repeating_character("aabbcc"))          # Expected Output: -1
print(first_non_repeating_character("simplilearn"))     # Expected Output: 0
```

## How to Run

1. Clone the Repository

 ```bash
git clone https://github.com/NikithaMatta/GlobalHackWeek-Career.git
```

2. Navigate to the Challenge01 folder:

```bash
cd globalhackweek/challenge-one
```

3. Run the Python code:
```bash
python First_Non_Repeating_Character.py
```
