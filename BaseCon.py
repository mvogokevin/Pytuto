def convert_base(number, original_base, target_base):
    decimal_number = 0
    
    # Convert the number from original base to decimal
    for digit in str(number):
        decimal_number = decimal_number * original_base + int(digit)
    
    # Convert the decimal number to the target base
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        converted_number = str(remainder) + converted_number
        decimal_number = decimal_number // target_base
    
    return converted_number

# Example usage
number = "101010"  # Number in original base
original_base = 2  # Original base (binary)
target_base = 8  # Target base (hexadecimal)

converted_number = convert_base(number, original_base, target_base)
print(f"The number {number} in base {original_base}\n is equivalent to {converted_number} in base {target_base}.")