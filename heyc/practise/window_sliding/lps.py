# def compute_lps(pattern):
#     """Preprocess the pattern to create the LPS (Longest Prefix Suffix) array."""
#     m = len(pattern)
#     lps = [0] * m
#     j = 0  # Length of previous longest prefix suffix
#     print(lps)
    
#     for i in range(1, m):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = lps[j - 1]

#         if pattern[i] == pattern[j]:
#             j += 1
#             lps[i] = j

#     return lps

# def kmp_search(text, pattern):
#     """Find all occurrences of the pattern in the text using KMP algorithm."""
#     n, m = len(text), len(pattern)
#     lps = compute_lps(pattern)
#     print(lps)
#     j = 0  # Index for pattern
#     occurrences = []

#     for i in range(n):
#         while j > 0 and text[i] != pattern[j]:
#             j = lps[j - 1]

#         if text[i] == pattern[j]:
#             j += 1

#         if j == m:
#             occurrences.append(i - m + 1)
#             j = lps[j - 1]  # Move j to the previous LPS value

#     return occurrences

# # Example Usage
# text = "abababcab"
# pattern = "ab"
# result = kmp_search(text, pattern)
# print("Pattern found at indices:", result)

# def compute_lps(pat):
#     n = len(pat)
#     lps = [0] * n  # Initialize LPS array
#     length = 0  # Length of the previous longest prefix suffix
#     i = 1  # Start from index 1

#     while i < n:
#         print(pat[i],pat[length])
#         if pat[i] == pat[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]  # Backtrack LPS value
#             else:
#                 lps[i] = 0
#                 i += 1
#         #print(lps,length)

#     return lps


def compute_lps(s):
    n = len(s)
    lps = [0] * n
    j = 0
    i = 1
    while i < n:
        print(j)
        if s[i] == s[j]:
            j +=1
            lps[i] = j
            i +=1
        else:
            if j != 0:
                print(lps)
                j = lps[j-1]
            lps[i] = 0
            i +=1
    print(lps)




print(compute_lps('ABABCABAB'))
