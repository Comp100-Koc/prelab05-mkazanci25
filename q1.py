def expand(s, l, r):
    
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    result = ""
    for i in range(len(s)):
        p1 = expand(s, i, i)
        p2 = expand(s, i, i + 1)
        
        for p in (p1, p2):
            if len(p) > len(result):
                result = p
    if len(result) >= 2:
        return result 
    else:
        return""