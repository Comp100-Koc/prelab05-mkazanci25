def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while adjacent_duplicates(s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                break 
    return s          
    
def adjacent_duplicates(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return True
    return False
