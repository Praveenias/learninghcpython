def countSubstrings(s, t):
    n, m = len(s), len(t)

    def test(i, j):
        res = pre = cur = 0
        for k in range(min(n - i, m - j)):
            cur += 1
            if s[i + k] != t[j + k]:
                pre, cur = cur, 0  # reset current, store previous segment length
            res += pre  # add all substrings that differ by exactly one char at this position
        return res

    # Start from each index in s against t starting from index 0
    # and each index in t against s starting from index 0 (excluding j=0 to avoid double counting)
    print(test(i, 0) for i in range(n))
    # return sum(test(i, 0) for i in range(n)) + sum(test(0, j) for j in range(1, m))

print(countSubstrings("aba","baba"))