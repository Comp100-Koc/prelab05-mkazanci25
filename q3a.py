def add_binary(a, b):
    decimal_sum = int(a, 2) + int(b, 2)
    
    if decimal_sum == 0:
        return "0b0"
    
    result = ""
    while decimal_sum > 0:
        kalan = decimal_sum % 2
        result = str(kalan) + result
        decimal_sum = decimal_sum // 2
        
    return "0b" + result