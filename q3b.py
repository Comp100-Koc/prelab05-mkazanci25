def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    s1 = a[2:]
    s2 = b[2:]
    
    result = ""
    carry = 0
    
    i = len(s1) - 1
    j = len(s2) - 1

    while i >= 0 or j >= 0 or carry:
        bit1 = 0
        if i >= 0:
            if s1[i] == '1':
                bit1 = 1
            i -= 1
            
        bit2 = 0
        if j >= 0:
            if s2[j] == '1':
                bit2 = 1
            j -= 1
            
        current_sum = bit1 + bit2 + carry
        
        if current_sum == 0:
            result = "0" + result
            carry = 0
        elif current_sum == 1:
            result = "1" + result
            carry = 0
        elif current_sum == 2:
            result = "0" + result
            carry = 1
        elif current_sum == 3:
            result = "1" + result
            carry = 1

    first_one = -1
    for k in range(len(result)):
        if result[k] == '1':
            first_one = k
            break
    
    if first_one == -1:
        return "0b0"
    
    return "0b" + result[first_one:]