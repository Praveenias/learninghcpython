from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"


from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    t_freq = Counter(t)  # Frequency map of t
    window_freq = {}  # Frequency map for current window
    required_chars = len(t_freq)  # Unique characters in t that need to be matched
    formed_chars = 0  # Number of characters matched with required frequency

    left, right = 0, 0
    min_len = float("inf")
    min_start = 0  # Starting index of the minimum substring

    while right < len(s):
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1

        if char in t_freq and window_freq[char] == t_freq[char]:
            formed_chars += 1  # When a required character is matched in exact frequency

        # Try to shrink from the left when all characters are matched
        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            left_char = s[left]
            window_freq[left_char] -= 1

            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                formed_chars -= 1  # A required character frequency goes below needed count

            left += 1  # Contract the window

        right += 1  # Expand the window
        print(formed_chars,s[min_start:right])

    return s[min_start:min_start + min_len] if min_len != float("inf") else ""


print(min_window("LAVARUSH", "LAVA"))