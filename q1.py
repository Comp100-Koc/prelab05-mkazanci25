def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    res = ""

    def expand(l, r):
        nonlocal res
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)

    return res if len(res) >= 2 else ""