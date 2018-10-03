# Recursive function that returns a string representing num in the base b

def convert(num, b):
    quotient = num // b
    return (convert(quotient, b) if quotient else '') + '0123456789ABCDEF'[num % b]